import numpy as np
from helpers import *


def read_candidates(fname):
    candidates = []
    with open(fname, 'r', encoding='utf-8') as f:
        candidates = f.readlines()
    return candidates


def modify_candidates(candidates, utterences, save='all'):
    new_candidates = []
    for candidate in candidates:
        candidate = candidate.split('1 ')[1][:-1]
        pattern, data = process_utterence(candidate)
        responses = utterences[pattern]
        for modified_response in set(utterences[pattern]):
            if save.isdigit() and responses[int(save)]!=modified_response:
                continue
            else:
                if pattern=='api_call':
                    new_candidates.append('1 ' + modified_response + data)
                elif pattern=='here it is':
                    if 'phone' in data:
                        d = data.split('_phone')[0]
                        new_candidates.append('1 ' + modified_response + d + '_1_phone')
                        new_candidates.append('1 ' + modified_response + d + '_1_social_media')
                        new_candidates.append('1 ' + modified_response + d + '_2_phone')
                        new_candidates.append('1 ' + modified_response + d + '_2_social_media')
                    elif 'address' in data:
                        d = data.split('_address')[0]
                        new_candidates.append('1 ' + modified_response + d + '_1_address' + d + '_1_public_transport')
                        new_candidates.append('1 ' + modified_response + d + '_1_address' + d + '_1_parking')
                        new_candidates.append('1 ' + modified_response + d + '_2_address' + d + '_2_public_transport')
                        new_candidates.append('1 ' + modified_response + d + '_2_address' + d + '_2_parking')
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
    candidates = read_candidates('../data/dialog-bAbI-tasks/dialog-babi-candidates.txt')
    new_candidates = modify_candidates(candidates, utterences)
    save_candidates(new_candidates, '../data/personalized-dialog-dataset/personalized-dialog-candidates.txt', True)

    new_candidates = modify_candidates(candidates, utterences, '0')
    save_candidates(new_candidates, '../data/personalized-dialog-dataset/split-by-profile/male_young/personalized-dialog-candidates.txt', True)

    new_candidates = modify_candidates(candidates, utterences, '1')
    save_candidates(new_candidates, '../data/personalized-dialog-dataset/split-by-profile/female_young/personalized-dialog-candidates.txt', True)

    new_candidates = modify_candidates(candidates, utterences, '2')
    save_candidates(new_candidates, '../data/personalized-dialog-dataset/split-by-profile/male_middle-aged/personalized-dialog-candidates.txt', True)

    new_candidates = modify_candidates(candidates, utterences, '3')
    save_candidates(new_candidates, '../data/personalized-dialog-dataset/split-by-profile/female_middle-aged/personalized-dialog-candidates.txt', True)

    new_candidates = modify_candidates(candidates, utterences, '4')
    save_candidates(new_candidates, '../data/personalized-dialog-dataset/split-by-profile/male_elderly/personalized-dialog-candidates.txt', True)

    new_candidates = modify_candidates(candidates, utterences, '5')
    save_candidates(new_candidates, '../data/personalized-dialog-dataset/split-by-profile/female_elderly/personalized-dialog-candidates.txt', True)

