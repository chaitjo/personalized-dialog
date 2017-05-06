import numpy as np
from helpers import *


def read_candidates(fname):
    candidates = []
    with open(fname, 'r', encoding='utf-8') as f:
        candidates = f.readlines()
    return candidates


def modify_candidates(candidates, utterences):
    new_candidates = []
    for candidate in candidates:
        candidate = candidate.split('1 ')[1][:-1]
        pattern, data = process_utterence(candidate)
        for modified_response in set(utterences[pattern]):
            if pattern=='api_call':
                new_candidates.append('1 ' + modified_response + data)   
            elif data:
                new_candidates.append('1 ' + modified_response + data + '_1')
                new_candidates.append('1 ' + modified_response + data + '_2')
            else : new_candidates.append('1 ' + modified_response)
    return new_candidates


def save_candidates(candidates, fname, shuffle=False):
    if shuffle:
        np.random.shuffle(candidates)
    with open(fname, 'w', encoding='utf-8') as f:
        for candidate in candidates:
            f.write(candidate+'\n')


if __name__ == '__main__':
    utterences = load_utterences()
    candidates = read_candidates('dialog-bAbI-tasks/dialog-babi-candidates.txt')
    new_candidates = modify_candidates(candidates, utterences)
    save_candidates(new_candidates, 'modified-tasks/modified-candidates.txt', True)