#!/usr/bin/env python

import tensorflow as tf

#=====================================================================================

def adamOptimizer(loss, learning_rate, var_list):
        batch = tf.Variable(0)
        optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step = batch, var_list = var_list)
        return optimizer

#=====================================================================================

class NetworkManager(object):

	def __init__(self):
		self.act_funcs = {'sigmoid':  tf.nn.sigmoid,
						  'softmax':  tf.nn.softmax,
						  'softsign': tf.nn.softsign,
						  'relu':     tf.nn.relu,
						  'tanh':     tf.nn.tanh,
						  'softplus': tf.nn.softplus}

	def get_weight(self, prefix, index):
		return getattr(self, 'weight_%d' % (index))

	def get_bias(self, prefix, index):
		return getattr(self, 'bias_%d' % (index))

	def get_func(self, prefix, index):
		return getattr(self, 'f_%d' % (index))

	def set_weight(self, prefix, index, weight):
		setattr(self, 'weight_%d' % (index), weight)

	def set_bias(self, prefix, index, bias):
		setattr(self, 'bias_%d' % (index), bias)

	def set_func(self, prefix, index, func):
		setattr(self, 'f_%d' % (index), func)


	def declare_mlp(self, prefix, layers, in_shape, hidden_shape, out_shape):
		self.set_weight(prefix, 0, tf.get_variable('weight_0', [in_shape, hidden_shape], initializer = tf.random_normal_initializer(0.01, 0.5), dtype = tf.float32))
		self.set_bias(prefix, 0, tf.get_variable('base_0', [hidden_shape], initializer = tf.constant_initializer(0.0), dtype = tf.float32))
		hidden     = -1
		for hidden in range(layers):
			self.set_weight(prefix, hidden + 1, tf.get_variable('weight_%d' % (hidden + 1), [hidden_shape, hidden_shape], initializer = tf.random_normal_initializer(0.01, 0.5), dtype = tf.float32))
			self.set_bias(prefix, hidden + 1, tf.get_variable('base_%d'   % (hidden + 1), [hidden_shape], initializer = tf.random_normal_initializer(0.0), dtype = tf.float32))
		self.set_weight(prefix, hidden + 2, tf.get_variable('weight_%d' % (hidden + 2), [hidden_shape, out_shape], initializer = tf.random_normal_initializer(0.01, 0.5), dtype = tf.float32))
		self.set_bias(prefix, hidden + 2, tf.get_variable('base_%d' % (hidden + 2), [out_shape], initializer = tf.constant_initializer(0.0), dtype = tf.float32))


	def connect_mlp_layers(self, prefix, layers, act_in, act_hidden, act_out, input_data):
		try:
			act_in     = self.act_funcs[act_in]
			act_hidden = self.act_funcs[act_hidden]
			act_out    = self.act_funcs[act_out]
		except KeyError:
			print 'ERROR: could not find activation functions %s, %s or %s' % (str(act_in), str(act_hidden), str(act_out)) 

		self.set_func(prefix, 0, act_in(tf.matmul(input_data, self.get_weight(prefix, 0)) + self.get_bias(prefix, 0)))
		hidden = -1
		for hidden in range(layers):
			self.set_func(prefix, hidden + 1, act_hidden(tf.matmul(self.get_func(prefix, hidden), self.get_weight(prefix, hidden + 1)) + self.get_bias(prefix, hidden + 1)))
		self.set_func(prefix, hidden + 2, act_out(tf.matmul(self.get_func(prefix, hidden + 1), self.get_weight(prefix, hidden + 2)) + self.get_bias(prefix, hidden + 2)))


#=====================================================================================

if __name__ == '__main__':
	pass
