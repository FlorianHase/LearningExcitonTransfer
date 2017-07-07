#!/usr/bin/env python

import hickle
import numpy as np 
import tensorflow as tf 

#=============================================================================================================================

ActivationFunctions = {descriptor: getattr(tf.nn, descriptor) for descriptor in ['softplus', 'relu', 'elu', 'softsign', 'sigmoid', 'tanh']}

#=============================================================================================================================

def mlp(inputData, out_dim, params):
	layerCount, neuronsPerLayer, activationFunction = params[0], params[1], params[2]

	weights = []
	bases = []
	dimensions = [inputData.get_shape()[1]]
	dimensions.extend([neuronsPerLayer for index in range(layerCount)])
	dimensions.append(out_dim)

	for layer in range(layerCount + 1):
		weight = tf.get_variable('weight_%d' % layer, [dimensions[layer], dimensions[layer + 1]], initializer = tf.random_normal_initializer(0.005, 0.001))
		base   = tf.get_variable('base_%d'   % layer, [dimensions[layer + 1]], initializer = tf.constant_initializer(0.0))
		weights.append(weight)
		bases.append(base)
	fcs = []
	for layer in range(layerCount + 1):
		if layer == layerCount:
			fc = tf.nn.softplus(tf.matmul(fcs[-1], weights[-1]) + bases[-1])
		elif layer == 0:
			fc = ActivationFunctions[activationFunction](tf.matmul(inputData, weights[layer]) + bases[layer])	
		else:
			fc = ActivationFunctions[activationFunction](tf.matmul(fcs[-1], weights[layer]) + bases[layer])
		fcs.append(fc)

	return fcs[-1], [fcs, weights, bases]

#=============================================================================================================================

class Predictor(NetworkManager):

	def __init__(self, network):
		self.network = network
		self._load_network_params()
	

	def _load_network_params(self):
		hyperparam_file = 'hyperparams_%s.hkl' % self.network
		hyperparams     = hickle.load(hyperparam_file)
		for hp_name, hp_value in hyperparams.items():
			setattr(self, str(hp_name), hp_value)


	def create_session(self, config = tf.ConfigProto()):

		with tf.variable_scope('N'):
			self.features = tf.placeholder(tf.float32, shape = (None, self.in_dim))
			self.targets  = tf.placeholder(tf.float32, shape = (None, self.out_dim))

			self.predictions = mlp(self.features, self.out_dim, [self.layers, self.hidden_dim, self.act])

		self.init_op = tf.global_variables_initializer()
		self.saver   = tf.train.Saver()
		self.session = tf.Session(config = config)
		self.session.run(self.init_op)


	def _restore(self, file_name = None):
		if not file_name:
			file_name = './Trained_MLPs/trained_mlp_%s' % self.network
		self.saver.restore(self.session, file_name)


	def predict(self, to_predict, out_file = 'prediction.dat'):
		self._restore()
		
		# load and rescale features
		self.pred_data    = hickle.load(to_predict)
		rescaled_features = (self.pred_data['features'] - self.lower_feature) / (self.upper_feature - self.lower_feature)

		prediction = self.session.run(self.predictions, {self.features: rescaled_features})
		prediction = np.array(prediction[0])
		prediction = prediction * (self.upper_target - self.lower_target) + self.lower_target

		# write predictions to file
		content = open(out_file, 'w')
		content.write('# index \t transfer time [ps] \t efficiency\n')
		for index, element in enumerate(prediction):
			content.write('%d\t%.5e\t%.5e\n' % (index, element[0], element[1]))
		content.close()

#=============================================================================================================================

if __name__ == '__main__':
	
	predictor = Predictor('CP43')
	predictor.create_session()
	predictor.predict('../../Database/ps2_cp43_times.hkl')