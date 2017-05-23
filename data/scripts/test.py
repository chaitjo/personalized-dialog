from helpers import *
from candidates import *

dialogs_set = [
    read_babi('modified-tasks/modified-task1-API-calls-dev.txt'),
    read_babi('modified-tasks/modified-task2-API-refine-dev.txt'),
    read_babi('modified-tasks/modified-task3-options-dev.txt'),
    read_babi('modified-tasks/modified-task4-info-dev.txt'),
    read_babi('modified-tasks/modified-task5-full-dialogs-dev.txt')
]

candidates = read_candidates('modified-tasks/modified-candidates.txt')

for dialogs in dialogs_set:
    for dialog in dialogs:
        for turn in dialog:
            if len(turn)==2:
                if '1 '+turn[1]+'\n' not in candidates:
                    print(turn)

print('OK')