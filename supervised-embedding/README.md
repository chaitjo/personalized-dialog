# Supervised Embeddings
Implementation of the Supervised Embeddings model from
[Learning End-to-End Goal-Oriented Dialog](https://arxiv.org/abs/1605.07683) in Tensorflow. Tested on the bAbI Dialog dataset and the Personalized Dialog dataset. 

Experimental logs and best performing models for each task can be downloaded using the `build_experiments.py` script.

Adapted from [sld's implementation](https://github.com/sld/supervised-embedding-model).

## Usage

Training the model on all the tasks
```
bin/train_all.sh
```

Testing the model on all the tasks
```
bin/test_all.sh
```

## Requirements

* tensorflow
* tqdm

## Results

### bAbI Dialog Tasks

<table>
  <tr>
    <td>
      Task
    </td>
    <td>
      Supervised Embedding (Article)
    </td>
    <td>
      Supervised Embedding (Ours)
    </td>
  </tr>
  <tr>
    <td>
      T1: Issuing API calls
    </td>
    <td>
      100
    </td>
    <td>
      99.6
    </td>
  </tr>
  <tr>
    <td>
      T2: Updating API calls
    </td>
    <td>
      68.4
    </td>
    <td>
      68.4
    </td>
  </tr>
  <tr>
    <td>
      T3: Displaying options
    </td>
    <td>
      64.9
    </td>
    <td>
      56.9
    </td>
  </tr>
  <tr>
    <td>
      T4: Providing information
    </td>
    <td>
      57.2
    </td>
    <td>
      57.1
    </td>
  </tr>
  <tr>
    <td>
      T5: Full Dialogs
    </td>
    <td>
      75.4
    </td>
    <td>
      62.1
    </td>
  </tr>
  <tr>
    <td>
      T6: Dialog state tracking 2
    </td>
    <td>
      22.6
    </td>
    <td>
      10.8
    </td>
  </tr>
</table>

### Personalized Dialog tasks (full set)

Task  |  Testing Accuracy  
------|---------------------
  1   |       84.37
  2   |       12.07
  3   |       9.21
  4   |       4.76
  5   |       51.60
