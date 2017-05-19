#!/bin/bash
source activate deep-learning
# python single_dialog.py --task_id 1
# python single_dialog.py --task_id 2
# python single_dialog.py --task_id 3
python single_dialog.py --task_id 4
# python single_dialog.py --task_id 5
# python single_dialog.py --task_id 1 --train False
# python single_dialog.py --task_id 2 --train False
# python single_dialog.py --task_id 3 --train False
python single_dialog.py --task_id 4 --train False
# python single_dialog.py --task_id 5 --train False
# python single_dialog.py --task_id 1 --train False --OOV True
# python single_dialog.py --task_id 2 --train False --OOV True
# python single_dialog.py --task_id 3 --train False --OOV True
python single_dialog.py --task_id 4 --train False --OOV True
# python single_dialog.py --task_id 5 --train False --OOV True
