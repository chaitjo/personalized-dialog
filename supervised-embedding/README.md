# Description

It is the implementation of Supervised embedding models from
[[Learning End-to-End Goal-Oriented Dialog](https://arxiv.org/abs/1605.07683v3)] paper.

Results almost the same as in the paper.

Here you can find Russian paper-note of the paper: [link](https://github.com/sld/deeplearning-papernotes/blob/master/notes/end-to-end-goal.md).

# Environment

* Python 3.6.0
* tensorflow 1.0.0
* Dialog bAbI Tasks Data 1-6 corpus, download by the [link](https://research.fb.com/downloads/babi/).
This corpus should be placed in data/dialog-bAbI-tasks directory.


All packages are listed in requirements.txt.

# Reproduce results

0. Setup the environment.
1. Run: `bin/train_all.sh`
2. After approx. 1 hour run it in test set: `bin/test_all.sh`


# Results

16.03.17.

In the table per-response accuracy is shown.

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
      T5: Full dialogs
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

Open question:

1. When we training with use_history=True should we test on pre-processed
dataset as in train? Or should we concat each output in test and build history
on the fly?
