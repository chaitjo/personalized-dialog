# from signal import signal, SIGPIPE, SIG_DFL
from sys import stdin

if __name__ == '__main__':
    # signal(SIGPIPE, SIG_DFL)

    fin = stdin
    vocab = set()
    for line in fin:
        splitted = line.strip().split('\t')
        if len(splitted) == 2:
            context, response = splitted
        elif len(splitted) == 1:
            context = ''
            response = splitted[0]
        else:
            raise ValueError("Wrong value {}".format(splitted))

        for w in context.split(' '):
            if w != '':
                vocab.add(w)

        for w in response.split(' '):
            if w != '':
                vocab.add(w)

    vocab = list(vocab)
    for i in range(len(vocab)):
        print('{}\t{}'.format(i, vocab[i]))
