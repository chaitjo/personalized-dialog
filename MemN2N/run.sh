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

python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_young/" --model_dir "model0/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_young/" --model_dir "model1/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_middle-aged/" --model_dir "model2/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_middle-aged/" --model_dir "model3/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_elderly/" --model_dir "model4/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_elderly/" --model_dir "model5/"
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_young/" --model_dir "model0/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_young/" --model_dir "model1/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_middle-aged/" --model_dir "model2/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_middle-aged/" --model_dir "model3/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/male_elderly/" --model_dir "model4/" --train False
python single_dialog.py --task_id 5 --data_dir "../data/modified-tasks/split/female_elderly/" --model_dir "model5/" --train False
