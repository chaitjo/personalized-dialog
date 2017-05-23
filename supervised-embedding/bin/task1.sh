#!/bin/bash

source bin/utils.sh

task="task-1"
mkdir -p checkpoints/$task/
WITH_PREPROCESS="$1"
[ -z "$WITH_PREPROCESS" ] && WITH_PREPROCESS='False'

if [ "$WITH_PREPROCESS" == "True" ]; then
	python parse_candidates.py ../data/modified-tasks/modified-candidates.txt > data/candidates.tsv
  parse_dialogs 'modified-task1-API-calls' $task '--with_history --ignore_options'
fi

python train.py --train data/train-$task.tsv --dev data/dev-$task-500.tsv \
  --vocab data/vocab-$task.tsv --save_dir checkpoints/$task/model
