from speech_style import *
from task3 import *


def modify_info(dialogs, kb, utterences):
    new_dialogs = []
    for dialog in dialogs:
        temp_dialog = [dialog[0]]
        profile = ['male young', 'female young', 'male middle-aged', 'female middle-aged', 'male elderly', 'female elderly'].index(dialog[0][0])

        restaurant = np.random.choice(get_restaurants(dialog, mode='modified'))
        attrib_list = ['R_phone', 'R_cuisine', 'R_address', 'R_location', 'R_number', 'R_price', 'R_rating', 'R_type', 'R_speciality', 'R_social_media', 'R_parking', 'R_public_transport']
        for attrib in attrib_list:
            temp_dialog.append([restaurant + ' ' + attrib + ' ' + kb[restaurant][attrib]])

        for turn in dialog:
            if len(turn) == 2:
                if restaurant[:-2] in turn[0]:
                	turn[0] = turn[0].replace(restaurant[:-2], restaurant)
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
    kb = read_kb('modified-tasks/modified-kb-all.txt')
    
    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task4-phone-address-dev.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task4-info-dev.txt')

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task4-phone-address-trn.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task4-info-trn.txt')

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task4-phone-address-tst.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task4-info-tst.txt')

    dialogs = read_babi('dialog-bAbI-tasks/dialog-babi-task4-phone-address-tst-OOV.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    new_dialogs = modify_info(new_dialogs, kb, utterences)
    save_babi(new_dialogs, 'modified-tasks/modified-task4-info-tst-OOV.txt')

