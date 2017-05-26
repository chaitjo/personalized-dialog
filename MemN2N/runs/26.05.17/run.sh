#!/bin/bash
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_young/" --train False --load_vocab True --memory_size 50
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_young/" --train False --load_vocab True --memory_size 50
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_middle-aged/" --train False --load_vocab True --memory_size 50
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_middle-aged/" --train False --load_vocab True --memory_size 50
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_elderly/" --train False --load_vocab True --memory_size 50
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_elderly/" --train False --load_vocab True --memory_size 50