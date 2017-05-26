from speech_style import *
from kb import *
from task3 import get_restaurants, rank_restaurants


def modify_options(dialogs, kb, accept_prob=0.25, save='all'):
    new_dialogs = []
    for dialog in dialogs:
        restaurants = get_restaurants(dialog)
        specialities = set([kb[restaurant]['R_speciality'] for restaurant in restaurants])
        temp_dialog_set = [[['veg ' + np.random.choice(list(specialities))]],
                           [['non-veg ' + np.random.choice(list(specialities))]]]
        for turn in dialog:
            if 'resto_' in turn[0] : break
            for temp_dialog in temp_dialog_set:
                temp_dialog.append(turn)

        for restaurant in restaurants:
            attrib_list = ['R_phone', 'R_cuisine', 'R_address', 'R_location', 'R_number', 'R_price', 'R_rating', 'R_type', 'R_speciality', 'R_social_media', 'R_parking', 'R_public_transport']
            for temp_dialog in temp_dialog_set:
                for attrib in attrib_list:
                    temp_dialog.append([restaurant + ' ' + attrib + ' ' + kb[restaurant][attrib]])

        # for turn in dialog:
        #     if len(turn) == 2:
        #         for temp_dialog in temp_dialog_set:
        #             temp_dialog.append(turn)
        #         if turn[1] == 'ok let me look into some options for you' : break

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

        for turn in dialog:
            temp_list = ['here it is', 'is there anything i can help you with', "you're welcome"]
            if len(turn) == 2:
                for item in temp_list:
                    if item in turn[1]:
                        for temp_dialog in temp_dialog_set:
                            temp_dialog.append(turn)

        if save=='random':
            new_dialogs.append(temp_dialog_set[np.random.choice(len(temp_dialog_set))])
        else:
            for temp_dialog in temp_dialog_set:
                new_dialogs.append(temp_dialog)
    return new_dialogs


def modify_info(dialogs, kb, utterences):
    new_dialogs = []
    for dialog in dialogs:
        profile = ['male young', 'female young', 'male middle-aged', 'female middle-aged', 'male elderly', 'female elderly'].index(' '.join(dialog[0][0].split(' ')[:2]))
        restaurant = ''
        for i, turn in enumerate(dialog):
            if len(turn) == 2:
                if utterences['what do you think of this option:'][profile] in turn[1] : restaurant = turn[1].split(': ')[1]
                elif turn[1] == utterences['great let me do the reservation'][profile] : break

        temp_dialog = dialog[:i]
        for turn in dialog[i:]:
            queries = {
                'contact' : ['do you have its contact details',
                            'may i have the contact details of the restaurant',
                            'what are the contact details of the restaurant'],
                'directions' : ['do you have direction information',
                            'may i have the direction information to the restaurant',
                            'can you provide direction to the restaurant']
            }
            if 'phone number' in turn[0]:
                turn[0] = np.random.choice(queries['contact'])
                if temp_dialog[0][0].split(' ')[1] == 'young':
                    turn[1] = utterences['here it is'][profile] + ' ' + kb[restaurant]['R_social_media']
                else:
                    turn[1] = utterences['here it is'][profile] + ' ' + kb[restaurant]['R_phone']
            if 'address' in turn[0]:
                turn[0] = np.random.choice(queries['directions'])
                if kb[restaurant]['R_price'] == 'cheap':
                    turn[1] = utterences['here it is'][profile] + ' ' + kb[restaurant]['R_address'] + ' ' + kb[restaurant]['R_public_transport']
                else:
                    turn[1] = utterences['here it is'][profile] + ' ' + kb[restaurant]['R_address'] + ' ' + kb[restaurant]['R_parking']
            temp_dialog.append(turn)
        new_dialogs.append(temp_dialog)
    return new_dialogs


if __name__ == '__main__':
    utterences = load_utterences()
    kb = read_kb('../modified-tasks/modified-kb-all.txt')

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task5-full-dialogs-dev.txt')

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task5-full-dialogs-trn.txt')

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task5-full-dialogs-tst.txt')

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb)
    new_dialogs = modify_speech_style(new_dialogs, utterences, 'modified')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task5-full-dialogs-tst-OOV.txt')

    # 1000 dialogs set
    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='random')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/1000/modified-task5-full-dialogs-dev.txt')

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='random')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/1000/modified-task5-full-dialogs-trn.txt')

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='random')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/1000/modified-task5-full-dialogs-tst.txt')

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='random')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/1000/modified-task5-full-dialogs-tst-OOV.txt')

    # Split dialog sets
    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='0')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_young/modified-task5-full-dialogs-dev.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='0')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_young/modified-task5-full-dialogs-trn.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='0')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_young/modified-task5-full-dialogs-tst.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='0')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_young/modified-task5-full-dialogs-tst-OOV.txt')


    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='1')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_young/modified-task5-full-dialogs-dev.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='1')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_young/modified-task5-full-dialogs-trn.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='1')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_young/modified-task5-full-dialogs-tst.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='1')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_young/modified-task5-full-dialogs-tst-OOV.txt')


    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='2')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_middle-aged/modified-task5-full-dialogs-dev.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='2')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_middle-aged/modified-task5-full-dialogs-trn.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='2')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_middle-aged/modified-task5-full-dialogs-tst.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='2')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_middle-aged/modified-task5-full-dialogs-tst-OOV.txt')


    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='3')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_middle-aged/modified-task5-full-dialogs-dev.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='3')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_middle-aged/modified-task5-full-dialogs-trn.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='3')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_middle-aged/modified-task5-full-dialogs-tst.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='3')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_middle-aged/modified-task5-full-dialogs-tst-OOV.txt')


    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='4')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_elderly/modified-task5-full-dialogs-dev.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='4')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_elderly/modified-task5-full-dialogs-trn.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='4')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_elderly/modified-task5-full-dialogs-tst.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='4')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/male_elderly/modified-task5-full-dialogs-tst-OOV.txt')


    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-dev.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='5')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_elderly/modified-task5-full-dialogs-dev.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-trn.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='5')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_elderly/modified-task5-full-dialogs-trn.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='5')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_elderly/modified-task5-full-dialogs-tst.txt')

    dialogs = dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task5-full-dialogs-tst-OOV.txt')
    new_dialogs = modify_options(dialogs, kb, save='random')
    new_dialogs = modify_speech_style(new_dialogs, utterences, setting='modified', save='5')
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, '../modified-tasks/split/female_elderly/modified-task5-full-dialogs-tst-OOV.txt')

