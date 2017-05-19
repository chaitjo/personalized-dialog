#!/bin/bash

source bin/utils.sh

task="task-5"
mkdir -p checkpoints/$task/
WITH_PREPROCESS="$1"
[ -z "$WITH_PREPROCESS" ] && WITH_PREPROCESS='False'

if [ "$WITH_PREPROCESS" == "True" ]; then
  python parse_candidates.py ../data/modified-tasks/modified-candidates.txt > data/candidates.tsv
  parse_dialogs 'modified-task5-full-dialogs' $task "--ignore_options --with_history"
fi

python train.py --train data/train-$task.tsv --dev data/dev-$task-500.tsv \
  --vocab data/vocab-$task.tsv --emb_dim 32 --save_dir checkpoints/$task/model \
  --margin 0.01 --negative_cand 100 --learning_rate 0.01
