from speech_style import *

if __name__ == '__main__':
    utterences = load_utterences()
    
    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task2-API-refine-dev.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task2-API-refine-dev.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task2-API-refine-trn.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task2-API-refine-trn.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task2-API-refine-tst.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task2-API-refine-tst.txt', True)

    dialogs = read_babi('../dialog-bAbI-tasks/dialog-babi-task2-API-refine-tst-OOV.txt')
    new_dialogs = modify_speech_style(dialogs, utterences)
    save_babi(new_dialogs, '../modified-tasks/modified-task2-API-refine-tst-OOV.txt', True)
