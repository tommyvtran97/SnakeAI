import numpy as np
import copy
from settings import *
"""

This script contains the Genetic Algorith. This algorithm contains
the selection of the parents for each generation, crossover to generate
new offsprings in the next generation and mutation of the offsprings
to create more variety of offsprings. 

"""

class Genetic_Algorithm(object):

	def __init__(self):
		pass

	def parents_selection(self, weights, bias, fitness):
		best_snakes_fitness = []
		best_snakes_idx 	= []
		parents_weights 	= []
		parents_bias		= []
		probability 		= []

		for _ in range(num_parents):
			top_snake_idx = fitness.index(max(fitness))

			best_snakes_fitness.append(max(fitness))
			best_snakes_idx.append(top_snake_idx)
			parents_weights.append(weights[top_snake_idx])
			parents_bias.append(bias[top_snake_idx])

			fitness.pop(top_snake_idx)
			weights.pop(top_snake_idx)
			bias.pop(top_snake_idx)

		sum_probability = 0
		fitness_percentage = np.divide(best_snakes_fitness, sum(best_snakes_fitness))
		for i in range(len(best_snakes_fitness)):
			sum_probability += fitness_percentage[i]					# Note that minimum fitscore is always 1
			probability.append(sum_probability)

		return (best_snakes_fitness, best_snakes_idx, parents_weights, parents_bias, probability)

	def uniform_crossover(self, parents_weights, parents_bias, probability):
		offspring_weights 	= []
		offspring_bias 		= []

		select_parent1		= True
		select_parent2		= True
		count = 0

		for i in range(num_offspring):
			while True:
				parent1 = np.random.uniform(0,1)
				parent2 = np.random.uniform(0,1)

				for j in range(len(probability)):
					if parent1 < probability[j]:
						if select_parent1:
							parent_idx1 = j
							select_parent1 = False
					if parent2 < probability[j]:
						if select_parent2:
							parent_idx2 = j
							select_parent2 = False

				select_parent1 = True
				select_parent2 = True
		
				if parent_idx1 != parent_idx2:
					weights_temp1 = []
					for k in range(len(layer)-1):
						weights_temp2 = np.empty((layer[k], layer[k+1]))
						for l in range(weights_temp2.shape[0]):
							for m in range(weights_temp2.shape[1]):
								if np.random.uniform(0,1) < 0.5:
									weights_temp2[l, m] = parents_weights[parent_idx1][k][l,m]
								else:
									weights_temp2[l, m] = parents_weights[parent_idx2][k][l,m]	
						weights_temp1.append(weights_temp2)
					offspring_weights.append(weights_temp1)

					bias_temp1 = []
					for k in range(len(layer)-1):
						bias_temp2 = np.empty((1, layer[k+1]))
						for l in range(bias_temp2.shape[0]):
							for m in range(bias_temp2.shape[1]):
								if np.random.uniform(0,1) < 0.5:
									bias_temp2[l, m] = parents_bias[parent_idx1][k][l,m]
								else:
									bias_temp2[l, m] = parents_bias[parent_idx2][k][l,m]	
						bias_temp1.append(bias_temp2)
					offspring_bias.append(bias_temp1)

					break

		return (offspring_weights, offspring_bias)

	def uniform_mutation(self, offspring_weights):
		offspring_weights_mutated = copy.deepcopy(offspring_weights)
		
		for i in range(num_offspring):
			for j in range(len(layer)-1):
				for k in range(layer[j]):
					for l in range(layer[j+1]):
						if np.random.uniform(0,1) < mutation_rate:
							offspring_weights_mutated[i][j][k,l] = np.random.choice(np.arange(-1, 1, step=0.01))
		
		return (offspring_weights_mutated)











		