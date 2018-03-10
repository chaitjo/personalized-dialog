# End-to-end Memory Networks with *Multi Memory* Architecture
Implementation of multi memory architecture for Memory Networks in Tensorflow. Tested on the personalized dialog dataset. 

Experimental logs and best performing models for each task can be downloaded using the `build_experiments.py` script.

Profile attributes, user utterances, bot responses and KB facts are modeled in four separate memories. The outputs from all memories are fused to get the final response.

## Usage

Train the model
```
python single_dialog.py --train True --task_id 1
```

Test the trained model
```
python single_dialog.py --train False --task_id 1
```

## Requirements

* tensorflow 0.12.1
* scikit-learn
* six
* scipy

## Results

### Personalized Dialog tasks (full set)

Task  |  Training Accuracy  |  Validation Accuracy  |  Testing Accuracy	 |  Testing Accuracy(OOV)
------|---------------------|-----------------------|--------------------|-----------------------

### Personalized Dialog tasks (small set)

Task  |  Training Accuracy  |  Validation Accuracy  |  Testing Accuracy	 |  Testing Accuracy(OOV)
------|---------------------|-----------------------|--------------------|-----------------------
