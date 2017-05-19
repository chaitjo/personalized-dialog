from sys import argv


def parse_candidates(filename):
    with open(filename, 'r') as f:
        return [' '.join(line.strip().split(' ')[1:]) for line in f]


if __name__ == '__main__':
    filename = argv[1]
    for cand in parse_candidates(filename):
        print('{}\t<SILENCE>'.format(cand))
