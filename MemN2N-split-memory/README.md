# End-to-end Memory Networks with *Split Memory* Architecture
Implementation of split memory architecture for Memory Networks described in [Personalization in Goal-oriented Dialog](https://arxiv.org/abs/1706.07503) in Tensorflow. Tested on the personalized dialog dataset. 

Experimental logs and best performing models for each task can be downloaded using the `build_experiments.py` script.

![Memory Network with split memory architecture](/img/memNN.png)

Profile attributes and conversation history are modeled in two separate memories. The outputs from both memories are summed to get the final response.

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
1	  |  87.06				|  85.36				|  85.66  			 |  66.60
2	  |  93.71				|  93.54				|  93.42			 |  76.04
3     |  99.97				|  67.62				|  68.60			 |  64.38
4	  |  100				|  56.67				|  57.17			 |  56.98
5	  |  95.38				|  87.01				|  87.28			 |  63.96

### Personalized Dialog tasks (small set)

Task  |  Training Accuracy  |  Validation Accuracy  |  Testing Accuracy	 |  Testing Accuracy(OOV)
------|---------------------|-----------------------|--------------------|-----------------------
1	  |  85.42				|  82.24				|  82.24  			 |  69.35
2	  |  94.47				|  93.08				|  91.27			 |  78.65
3     |  97.86				|  67.35				|  68.01			 |  65.88
4	  |  99.48				|  56.61				|  57.11			 |  56.98
5	  |  97.20				|  77.10				|  78.10			 |  61.40
