#!/bin/bash

echo "Task-1 on test set"
python test.py --test data/test-task-1.tsv --candidates data/candidates.tsv \
  --vocab data/vocab-task-1.tsv --checkpoint_dir checkpoints/task-1 --emb_dim 32

echo "Task-2 on test set"
python test.py --test data/test-task-2.tsv --candidates data/candidates.tsv \
  --vocab data/vocab-task-2.tsv --checkpoint_dir checkpoints/task-2 --emb_dim 128

echo "Task-3 on test set"
python test.py --test data/test-task-3.tsv --candidates data/candidates.tsv \
  --vocab data/vocab-task-3.tsv --checkpoint_dir checkpoints/task-3 --emb_dim 128

echo "Task-4 on test set"
python test.py --test data/test-task-4.tsv --candidates data/candidates.tsv \
  --vocab data/vocab-task-4.tsv --checkpoint_dir checkpoints/task-4 --emb_dim 128

echo "Task-5 on test set"
python test.py --test data/test-task-5.tsv --candidates data/candidates.tsv \
  --vocab data/vocab-task-5.tsv --checkpoint_dir checkpoints/task-5 --emb_dim 32
