# Personalization in Goal-Oriented Dialog
This repository contains code for the paper ["Personalization in Goal-Oriented Dialog"](https://www.dropbox.com/s/d8e8ap0sd9co98s/Personalization_in_Goal-Oriented_Dialog.pdf?dl=1) by Chaitanya Joshi, Fei Mi and Boi Faltings. We introduce a set of 5 tasks for testing end-to-end dialog systems in a goal-oriented setting with a focus on personalization of conversation. We also provide baselines using various models and publicize our implementations and experimental results through this repository.

## Dataset
The Personalized dialog dataset can be downloaded using `build_data.py`. Alternatively, it is accessable using [this link](https://www.dropbox.com/s/4i9u4y24pt3paba/personalized-dialog-dataset.tar.gz?dl=1) or through the [ParlAI](http://parl.ai/) framework for dialog AI research. 

Each of the tasks can also be generated from the bAbI dialog tasks using the files in the `scripts/` directory.

## Models
We provide our implementations of two models- Memory Networks (`MemN2N/`) and Supervised Embeddings (`supervised-embedding/`). Each directory contains scripts, experimental logs and model checkpoints. Instructions on using a models are given in its README.
