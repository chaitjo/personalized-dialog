import tensorflow as tf
import numpy as np
import argparse
import logging
import sys
from tqdm import tqdm
from make_tensor import make_tensor, load_vocab
from model import Model
from sys import argv
from test import evaluate
from utils import batch_iter, neg_sampling_iter


def _setup_logger():
    logging.basicConfig(
        format='[%(levelname)s] %(asctime)s: %(message)s (%(pathname)s:%(lineno)d)',
        datefmt="%Y-%m-%dT%H:%M:%S%z",
        stream=sys.stdout)
    logger = logging.getLogger('babi-dialog')
    logger.setLevel(logging.DEBUG)
    return logger


logger = _setup_logger()


def _parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--train', help='Path to train filename')
    parser.add_argument('--dev', help='Path to dev filename')
    parser.add_argument('--vocab', default='data/vocab.tsv')
    parser.add_argument('--candidates', default='data/candidates.tsv')
    parser.add_argument('--emb_dim', default=32, type=int)
    parser.add_argument('--save_dir')
    parser.add_argument('--margin', type=float, default=0.01)
    parser.add_argument('--negative_cand', type=int, default=100)
    parser.add_argument('--learning_rate', type=float, default=0.01)

    args = parser.parse_args()

    return args


def _train(train_tensor, batch_size, neg_size, model, optimizer, sess):
    avg_loss = 0
    for batch in batch_iter(train_tensor, batch_size, True):
        for neg_batch in neg_sampling_iter(train_tensor, batch_size, neg_size):
            loss = sess.run(
                [model.loss, optimizer],
                feed_dict={model.context_batch: batch[:, 0, :],
                           model.response_batch: batch[:, 1, :],
                           model.neg_response_batch: neg_batch[:, 1, :]}
            )
            avg_loss += loss[0]
    avg_loss = avg_loss / (train_tensor.shape[0]*neg_size)
    return avg_loss


def _forward_all(dev_tensor, model, sess):
    avg_dev_loss = 0
    for batch in batch_iter(dev_tensor, 256):
        for neg_batch in neg_sampling_iter(dev_tensor, 256, 1, 42):
            loss = sess.run(
                [model.loss],
                feed_dict={model.context_batch: batch[:, 0, :],
                           model.response_batch: batch[:, 1, :],
                           model.neg_response_batch: neg_batch[:, 1, :]}
            )
            avg_dev_loss += loss[0]
    avg_dev_loss = avg_dev_loss / (dev_tensor.shape[0]*1)
    return avg_dev_loss


def main(train_tensor, dev_tensor, candidates_tensor, model, config):
    logger.info('Run main with config {}'.format(config))

    epochs = config['epochs']
    batch_size = config['batch_size']
    negative_cand = config['negative_cand']
    save_dir = config['save_dir']

    # TODO: Add LR decay
    optimizer = tf.train.AdamOptimizer(config['lr']).minimize(model.loss)

    prev_best_accuracy = 0

    saver = tf.train.Saver()
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:
        sess.run(tf.global_variables_initializer())

        for epoch in range(epochs):
            avg_loss = _train(train_tensor, batch_size, negative_cand, model, optimizer, sess)
            # TODO: Refine dev loss calculation
            avg_dev_loss = _forward_all(dev_tensor, model, sess)
            logger.info('Epoch: {}; Train loss: {}; Dev loss: {};'.format(epoch, avg_loss, avg_dev_loss))

            if epoch % 2 == 0:
                dev_eval = evaluate(dev_tensor, candidates_tensor, sess, model)
                logger.info('Evaluation: {}'.format(dev_eval))
                accuracy = dev_eval[2]
                if accuracy >= prev_best_accuracy:
                    logger.debug('Saving checkpoint')
                    prev_best_accuracy = accuracy
                    saver.save(sess, save_dir)


if __name__ == '__main__':
    args = _parse_args()
    vocab = load_vocab(args.vocab)
    train_tensor = make_tensor(args.train, vocab)
    dev_tensor = make_tensor(args.dev, vocab)
    candidates_tensor = make_tensor(args.candidates, vocab)
    config = {'batch_size': 32, 'epochs': 15,
              'negative_cand': args.negative_cand, 'save_dir': args.save_dir,
              'lr': args.learning_rate}
    model = Model(len(vocab), emb_dim=args.emb_dim, margin=args.margin)
    main(train_tensor, dev_tensor, candidates_tensor, model, config)
