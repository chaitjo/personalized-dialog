import numpy as np
from speech_style import *
from kb import *


def get_restaurants(dialog, shuffle=True):
    old_restaurants = []
    for turn in dialog:
        if len(turn) == 1:
            old_restaurants.append(turn[0].split(' ')[0])

    old_restaurants = set(old_restaurants)

    new_restaurants = []
    for restaurant in old_restaurants:
        new_restaurants.append(restaurant+'_1')
        new_restaurants.append(restaurant+'_2')
    np.random.shuffle(new_restaurants)
    return new_restaurants


def rank_restaurants(restaurants, diet, fav_item, kb):
    ranked = {}
    for restaurant in restaurants:
        ranked[restaurant] = int(kb[restaurant]['R_rating'])
        if diet == kb[restaurant]['R_type']:
            ranked[restaurant] += 8.0
        if fav_item == kb[restaurant]['R_speciality']:
            ranked[restaurant] += 2.5

    def getItem(item) : return ranked[item]
    return sorted(ranked, key=getItem, reverse=True)


def modify_options(dialogs, kb, accept_prob=0.25):
    new_dialogs = []
    for dialog in dialogs:
        restaurants = get_restaurants(dialog)
        specialities = set([kb[restaurant]['R_speciality'] for restaurant in restaurants])

        temp_dialog_set = [[['veg ' + np.random.choice(list(specialities))]],
                           [['non-veg ' + np.random.choice(list(specialities))]]]

        for restaurant in restaurants:
            attrib_list = ['R_phone', 'R_cuisine', 'R_address', 'R_location', 'R_number', 'R_price', 'R_rating', 'R_type', 'R_speciality']
            for temp_dialog in temp_dialog_set:
                for attrib in attrib_list:
                    temp_dialog.append([restaurant + ' ' + attrib + ' ' + kb[restaurant][attrib]])

        for turn in dialog:
            if len(turn) == 2:
                for temp_dialog in temp_dialog_set:
                    temp_dialog.append(turn)
                if turn[1] == 'ok let me look into some options for you' : break

        for temp_dialog in temp_dialog_set:
            utterences = {
                        'reject' : ["do you have something else",
                                    "no i don't like that",
                                    "no this does not work for me"],
                        'accept' : ["that looks great",
                                    "i love that",
                                    "let's do it",
                                    "it's perfect"]
                          }
            ranked_restaurants = rank_restaurants(restaurants, temp_dialog[0][0].split(' ')[0], temp_dialog[0][0].split(' ')[1], kb)
            for restaurant in ranked_restaurants:
                temp_dialog.append(['<SILENCE>', 'what do you think of this option: ' + restaurant])
                if restaurant == ranked_restaurants[-1] : choice = 'accept'
                else : choice = np.random.choice(['accept', 'reject'], p=[accept_prob, 1-accept_prob])

                if choice == 'accept':
                    temp_dialog.append([np.random.choice(utterences['accept']), 'great let me do the reservation'])
                    break
                else :
                    temp_dialog.append([np.random.choice(utterences['reject']), 'sure let me find an other option for you'])

            new_dialogs.append(temp_dialog)
    return new_dialogs


if __name__ == '__main__':
    utterences = load_utterences()
    kb = read_kb('modified-tasks/modified-kb-all.txt')

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task3-options-dev.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    save_babi(new_dialogs, 'modified-tasks/modified-task3-options-dev.txt')

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task3-options-trn.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    save_babi(new_dialogs, 'modified-tasks/modified-task3-options-trn.txt')

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task3-options-tst.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    save_babi(new_dialogs, 'modified-tasks/modified-task3-options-tst.txt')

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task3-options-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    save_babi(new_dialogs, 'modified-tasks/modified-task3-options-tst-OOV.txt')
