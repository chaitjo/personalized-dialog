 #!/bin/bash

source bin/utils.sh

task="task-4"
mkdir -p checkpoints/$task/
WITH_PREPROCESS="$1"
[ -z "$WITH_PREPROCESS" ] && WITH_PREPROCESS='False'

if [ "$WITH_PREPROCESS" == "True" ]; then
  python parse_candidates.py ../data/modified-tasks/modifed-candidates.txt > data/candidates.tsv
  parse_dialogs 'modified-task4-info' $task "--ignore_options"
fi

python train.py --train data/train-$task.tsv --dev data/dev-$task-500.tsv \
  --vocab data/vocab-$task.tsv --emb_dim 128 --save_dir checkpoints/$task/model \
  --margin 0.1 --negative_cand 1000 --learning_rate 0.001
