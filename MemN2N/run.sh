#!/bin/bash
# python single_dialog.py --task_id 1
# python single_dialog.py --task_id 2
# python single_dialog.py --task_id 3
# python single_dialog.py --task_id 4
# python single_dialog.py --task_id 5
# python single_dialog.py --task_id 1 --train False
# python single_dialog.py --task_id 2 --train False
# python single_dialog.py --task_id 3 --train False
# python single_dialog.py --task_id 4 --train False
# python single_dialog.py --task_id 5 --train False
# python single_dialog.py --task_id 1 --train False --OOV True
# python single_dialog.py --task_id 2 --train False --OOV True
# python single_dialog.py --task_id 3 --train False --OOV True
# python single_dialog.py --task_id 4 --train False --OOV True
# python single_dialog.py --task_id 5 --train False --OOV True

python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_young/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_young/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_middle-aged/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_middle-aged/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_elderly/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_elderly/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_young/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_young/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_middle-aged/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_middle-aged/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_elderly/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_elderly/" --train False