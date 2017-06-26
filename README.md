# Personalization in Goal-Oriented Dialog
This repository contains code for the paper ["Personalization in Goal-Oriented Dialog"](https://arxiv.org/abs/1706.07503) by Chaitanya Joshi, Fei Mi and Boi Faltings. We introduce a set of 5 tasks for testing end-to-end dialog systems in a goal-oriented setting with a focus on personalization of conversation. We also provide baselines using various models and publicize our implementations and experimental results through this repository.

## Dataset
The Personalized Dialog dataset can be downloaded using `build_data.py`. Alternatively, it is accessable using [this link](https://www.dropbox.com/s/4i9u4y24pt3paba/personalized-dialog-dataset.tar.gz?dl=1) or through the [ParlAI](http://parl.ai/) framework for dialog AI research. 

Each of the tasks can also be generated from the [bAbI Dialog tasks](https://research.fb.com/projects/babi/) using the files in the `scripts/` directory.

## Models
We provide our implementations of two models- Memory Networks (`MemN2N/`) and Supervised Embeddings (`supervised-embedding/`). Each directory contains scripts, experimental logs and model checkpoints. Instructions on using a models are given in its README.

## References
* Antoine Bordes, Y-Lan Boureau, Jason Weston, "Learning End-to-End Goal-Oriented Dialog", [arXiv:1605.07683](https://arxiv.org/abs/1605.07683) [cs.CL].
* Chaitanya K. Joshi, Fei Mi, Boi Faltings, "Personalization in Goal-Oriented Dialog", [arXiv:1706.07503](https://arxiv.org/abs/1706.07503) [cs.CL].
