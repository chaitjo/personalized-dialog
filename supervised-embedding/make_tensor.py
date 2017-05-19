import numpy as np
from sys import argv


def vectorize_utt(utt, vocab):
    vec = np.zeros(len(vocab))
    for w in utt.split(' '):
        try:
            vec[vocab[w]] = 1
        except KeyError:
            pass
    return vec


def vectorize_all(context_response_pairs, vocab):
    tensor = np.ndarray((len(context_response_pairs), 2, len(vocab)))

    for ind, context_response in enumerate(context_response_pairs):
        context, response = context_response
        context_vec = vectorize_utt(context, vocab)
        response_vec = vectorize_utt(response, vocab)
        tensor[ind][0] = context_vec
        tensor[ind][1] = response_vec

    return tensor


def load_vocab(vocab_filename):
    vocab = {}
    with open(vocab_filename, 'r') as f:
        for line in f:
            ind, word = line.strip().split('\t')
            vocab[word] = int(ind)
    return vocab


def load_train(train_filename):
    context_response_pairs = []
    with open(train_filename, 'r') as f:
        for line in f:
            context, response = line.strip().split('\t')
            context_response_pairs.append((context, response))
    return context_response_pairs


def make_tensor(train_filename, vocab):
    if type(vocab) == 'str':
        vocab = load_vocab(vocab_filename)
    train = load_train(train_filename)
    X = vectorize_all(train, vocab)
    print(train_filename, X.shape)
    return X


if __name__ == '__main__':
    train_filename = argv[1]
    vocab_filename = argv[2]
    main(train_filename, vocab_filename)
