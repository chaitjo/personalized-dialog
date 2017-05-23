from helpers import *


def process_utterence(utterence):
    patterns = ['api_call', 'what do you think of this option:', 'here it is']
    for pattern in patterns:
        if pattern in utterence:
            return(pattern, utterence.split(pattern)[1])
    return (utterence, '')


def modify_speech_style(dialogs, utterences, setting='babi'):
    new_dialogs = []
    profiles = ['male young', 'female young', 'male middle-aged', 'female middle-aged', 'male elderly', 'female elderly']
    for dialog in dialogs:
        temp_dialog_set = []
        if setting=='modified':
            for profile in profiles:
                temp_dialog_set.append([[profile + ' ' + dialog[0][0]]])
            dialog = dialog[1:]
        else:
            for profile in profiles:
                temp_dialog_set.append([[profile]])

        for turn in dialog:
            if len(turn) > 1:
                temp_turn = []
                pattern, data = process_utterence(turn[1])
                for i, modified_response in enumerate(utterences[pattern]): # change this to patterns
                    temp_turn = [turn[0], modified_response + data]
                    temp_dialog_set[i].append(temp_turn)
            else:
                for i in range(len(temp_dialog_set)):
                    temp_dialog_set[i].append(turn)
        for temp_dialog in temp_dialog_set:
            new_dialogs.append(temp_dialog)
    return new_dialogs
