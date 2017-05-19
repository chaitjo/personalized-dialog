from make_tensor import make_tensor, load_vocab
from model import Model
from sys import argv
from utils import batch_iter
from tqdm import tqdm
import numpy as np
import tensorflow as tf
import argparse


def main(test_tensor, candidates_tensor, model, checkpoint_dir):
    saver = tf.train.Saver()
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:
        sess.run(tf.global_variables_initializer())
        ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
        saver.restore(sess, ckpt.model_checkpoint_path)
        print(evaluate(test_tensor, candidates_tensor, sess, model))


def evaluate(test_tensor, candidates_tensor, sess, model):
    neg = 0
    pos = 0
    for row in tqdm(test_tensor):
        true_context = [row[0]]
        test_score = sess.run(
            model.f_pos,
            feed_dict={model.context_batch: true_context,
                       model.response_batch: [row[1]],
                       model.neg_response_batch: [row[1]]}
        )
        test_score = test_score[0]

        is_pos = evaluate_one_row(candidates_tensor, true_context, sess, model, test_score, row[1])
        if is_pos:
            pos += 1
        else:
            neg += 1
    return (pos, neg, pos / (pos+neg))


def evaluate_one_row(candidates_tensor, true_context, sess, model, test_score, true_response):
    for batch in batch_iter(candidates_tensor, 512):
        candidate_responses = batch[:, 0, :]
        context_batch = np.repeat(true_context, candidate_responses.shape[0], axis=0)

        scores = sess.run(
            model.f_pos,
            feed_dict={model.context_batch: context_batch,
                       model.response_batch: candidate_responses,
                       model.neg_response_batch: candidate_responses}
        )
        for ind, score in enumerate(scores):
            if score == float('Inf') or score == -float('Inf') or score == float('NaN'):
                print(score, ind, scores[ind])
                raise ValueError
            if score >= test_score and not np.array_equal(candidate_responses[ind], true_response):
                return False
    return True


def _parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--test', help='Path to test filename')
    parser.add_argument('--vocab', default='data/vocab.tsv')
    parser.add_argument('--candidates', default='data/candidates.tsv')
    parser.add_argument('--checkpoint_dir')
    parser.add_argument('--emb_dim', type=int, default=32)

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = _parse_args()
    vocab = load_vocab(args.vocab)
    test_tensor = make_tensor(args.test, vocab)
    candidates_tensor = make_tensor(args.candidates, vocab)
    model = Model(len(vocab), args.emb_dim)
    main(test_tensor, candidates_tensor, model, args.checkpoint_dir)
