import numpy as np
from settings import *

class Neural_Network(object):

	def __init__(self, weights=None, bias=None):
		self.layer 			= layer
		self.weights_size 	= weights_size
		self.bias_size 		= bias_size
		self.weights 		= []
		self.bias 			= []

		if weights is None:
			for k in range(num_individuals):
				weights_temp = []
				for i in range(len(layer)-1):
					weights_temp.append(np.random.choice(np.arange(-1, 1, step=0.001), size=(layer[i], layer[i+1])))
				self.weights.append(weights_temp)
		else:
			self.weights = weights

		if bias is None:
			for _ in range(num_individuals):
				bias_temp = []
				for i in range(1, len(layer)):
					bias_temp.append(np.random.choice(np.arange(-1, 1, step=0.001), size=(1, layer[i])))
				self.bias.append(bias_temp)
		else:
			self.bias = bias

	def feed_forward(self, X):
		output_layer1 = self.relu(np.dot(X, self.weights[0]) + self.bias[0])

		current_layer = output_layer1
		if len(self.weights) > 2:
			for i in range(1, len(self.weights)-1):
				print(np.dot(current_layer, self.weights[i]) + self.bias[i])
				output_hidden = self.relu(np.dot(current_layer, self.weights[i]) + self.bias[i])
				current_layer = output_hidden

		output = self.sigmoid(np.dot(current_layer, self.weights[-1]) + self.bias[-1])

		return (np.argmax(output))

	def relu(self, matrix):
		relu = np.maximum(0, matrix)

		return (relu)

	def sigmoid(self, matrix):
		sigmoid = 1 / (1 + np.exp(-matrix))

		return (sigmoid)

# np.random.seed(0)
# X = np.array([0,0,0,1])
# NN = Neural_Network()
# W = NN.weights[1][1]
# B = NN.bias



