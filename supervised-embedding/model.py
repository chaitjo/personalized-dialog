import tensorflow as tf
import math
import numpy as np


class Model:
    def __init__(self, vocab_dim, emb_dim, margin=0.01):
        self._vocab_dim = vocab_dim
        self._emb_dim = emb_dim
        self._random_seed = 42
        self._margin = margin
        self._assemble_graph()

    def _assemble_graph(self):
        self._create_placeholders()
        tf.set_random_seed(self._random_seed + 1)

        A_var = tf.Variable(
            initial_value=tf.random_uniform(
                shape=[self._emb_dim, self._vocab_dim],
                minval=-1, maxval=1, seed=(self._random_seed + 2)
            )
        )
        B_var = tf.Variable(
            initial_value=tf.random_uniform(
                shape=[self._emb_dim, self._vocab_dim],
                minval=-1, maxval=1, seed=(self._random_seed + 3)
            )
        )
        self.global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name='global_step')

        cont_mult = tf.transpose(tf.matmul(A_var, tf.transpose(self.context_batch)))
        resp_mult = tf.matmul(B_var, tf.transpose(self.response_batch))
        neg_resp_mult = tf.matmul(B_var, tf.transpose(self.neg_response_batch))

        pos_raw_f = tf.diag_part(tf.matmul(cont_mult, resp_mult))
        neg_raw_f = tf.diag_part(tf.matmul(cont_mult, neg_resp_mult))
        self.f_pos = pos_raw_f
        self.f_neg = neg_raw_f

        self.loss = tf.reduce_sum(tf.nn.relu(self.f_neg - self.f_pos + self._margin))

    def _create_placeholders(self):
        self.context_batch = tf.placeholder(dtype=tf.float32, name='Context', shape=[None, self._vocab_dim])
        self.response_batch = tf.placeholder(dtype=tf.float32, name='Response', shape=[None, self._vocab_dim])
        self.neg_response_batch = tf.placeholder(dtype=tf.float32, name='NegResponse', shape=[None, self._vocab_dim])

    # TODO: Implement summaries
    def _init_summaries(self):
        self.accuracy = tf.placeholder_with_default(0.0, shape=(), name='Accuracy')
        self.accuracy_summary = tf.scalar_summary('Accuracy summary', self.accuracy)

        self.f_pos_summary = tf.histogram_summary('f_pos', self.f_pos)
        self.f_neg_summary = tf.histogram_summary('f_neg', self.f_neg)

        self.loss_summary = tf.scalar_summary('Mini-batch loss', self.loss)
        self.summary_op = tf.merge_summary(
            [
                self.f_pos_summary,
                self.f_neg_summary,
                self.loss_summary
            ]
        )
