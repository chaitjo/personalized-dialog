from speech_style import *

if __name__ == '__main__':
    utterences = load_utterences()

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-dev.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task1-API-calls-dev.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-trn.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task1-API-calls-trn.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-tst.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task1-API-calls-tst.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-tst-OOV.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task1-API-calls-tst-OOV.txt', True)

    # small dialogs set
    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-dev.txt')
    new_dialogs = modify_speech_style(dialogs, utterences, save='random')
    save_babi(new_dialogs, '../modified-tasks/small/modified-task1-API-calls-dev.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-trn.txt')
    new_dialogs = modify_speech_style(dialogs, utterences, save='random')
    save_babi(new_dialogs, '../modified-tasks/small/modified-task1-API-calls-trn.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-tst.txt')
    new_dialogs = modify_speech_style(dialogs, utterences, save='random')
    save_babi(new_dialogs, '../modified-tasks/small/modified-task1-API-calls-tst.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task1-API-calls-tst-OOV.txt')
    new_dialogs = modify_speech_style(dialogs, utterences, save='random')
    save_babi(new_dialogs, '../modified-tasks/small/modified-task1-API-calls-tst-OOV.txt', True)
