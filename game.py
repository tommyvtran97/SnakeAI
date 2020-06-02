import numpy as np
import pygame as pg 
from settings import *
from neural_network import *
from snake import *
from genetic_algorithm import *

class Game(object):

	def __init__(self, weights, bias):
		self.NN_initial = Neural_Network(weights, bias)
		self.weights 	= self.NN_initial.weights
		self.bias 		= self.NN_initial.bias
		self.fitness    = []

	def run_game(self, highscore, generation, top_snake=None, highscore_gen=0, individual=1, points=0, flag=True, show_best=False):

		if graphics_training or top_snake is not None:
			pg.init()
			pg.display.set_caption('Snake Game created by T.Tran')
			clock = pg.time.Clock()
		pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, snake_head, points, steps_taken, steps_left = self.restart_game()

		while flag:
			if top_snake is not None:
				if top_snake[generation-1] == individual-1:
					show_best = True
				else:
					show_best = False
			if graphics_training or show_best:
				clock.tick(30)
			SNAKE = Snake(pos_x, pos_y, self.weights[individual-1], self.bias[individual-1], show_best)
			snake_head, snake_list = SNAKE.draw(snake_list, snake_length, food_pos_x, food_pos_y, dx,dy)
			X = SNAKE.vision(food_pos_x, food_pos_y, snake_list)
			pos_x, pos_y, dx, dy, flag = SNAKE.move_snake(dx, dy, X, AI)
			snake_length, food_pos_x, food_pos_y, points, steps_left = SNAKE.eat(snake_list, snake_length, food_pos_x, food_pos_y, points, steps_left)

			if dx != 0 or dy != 0:
				steps_taken += 1
				steps_left 	-= 1

			fitscore = self.fitness_score(points, steps_taken)
			if graphics_training or show_best:
				self.draw_score(points, highscore, generation, individual, steps_left, fitscore)

			if self.out_of_bound(pos_x, pos_y) or self.head_body_collision(snake_head, snake_list) or steps_left == 0:
				self.fitness.append(fitscore)

				if self.out_of_bound(pos_x, pos_y):
					if graphics_training or show_best:
						pg.display.update()

				if points > highscore:
					highscore = points
				if points > highscore_gen:
					highscore_gen = points
				if individual == num_individuals:
					break

				pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, snake_head, points, steps_taken, steps_left = self.restart_game()
				individual += 1
				continue

			if graphics_training or show_best:
				pg.display.update()

		return (self.weights, self.bias, self.fitness, highscore, highscore_gen)

	def out_of_bound(self, pos_x, pos_y, collision=False):
		if pos_x < 0 or pos_x > display_width - snake_size or pos_y < offset or pos_y > display_height - snake_size:
			collision = True

		return (collision)

	def head_body_collision(self, snake_head, snake_list, collision=False):
		for x in snake_list[:-1]:
			if x == snake_head:
				collision = True
				break

		return (collision)

	def fitness_score(self, points, steps_taken):
		fitscore = steps_taken + (2**points + 500 * points**2.1) - (0.25 * steps_taken**1.3 * points**1.2)

		return (fitscore)

	def draw_score(self, points, highscore, generation, individual, steps_left, fitscore):
		smallfont = pg.font.SysFont(None, 25)
		text_1 = smallfont.render("Score: {} Snake: {} Generation: {}".format(points, individual, generation), True, [0,0,0])
		text_2 = smallfont.render("Highscore: {}".format(highscore), True, [0,0,0])
		screen.blit(text_1, [0,0])
		screen.blit(text_2, [display_width-120,0])

	def restart_game(self, food=True):
		pos_x 		= display_width / 2
		pos_y 		= display_height / 2

		points 		= 0
		steps_taken = 0
		steps_left 	= 200

		snake_head  = [pos_x, pos_y]

		dx 			= 0
		dy 			= 0

		snake_list = [[pos_x, pos_y+2*snake_size], [pos_x, pos_y+1*snake_size], [pos_x, pos_y]]

		while food:
			food_pos_x = np.random.choice(np.arange(0, display_width, step=snake_size))
			food_pos_y = np.random.choice(np.arange(offset, display_height, step=snake_size))
			for x in snake_list:
				if x[0] == food_pos_x and x[1] == food_pos_y:
					food = True
					break
				else:
					food = False

		return (pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, snake_head, points, steps_taken, steps_left)

if __name__ == "__main__":
	if train:
		seed = np.random.randint(10000)
		np.random.seed(seed)								# Use 0 for reference!
		highscore 	= 0
		weights 	= None
		bias 		= None

		top_snake_idx = []

		for generation in range(num_generations):
			start = Game(weights, bias)
			weights, bias, fitness, highscore, highscore_gen = start.run_game(highscore, (generation+1))

			top_snake_idx.append(fitness.index(max(fitness)))

			print ('Generation: {} - Mean Fitness: {} - Max Fitness: {} - Score: {}'.format((generation+1), np.round(np.mean(fitness), 2), np.round(np.max(fitness), 2), highscore_gen))

			GA = Genetic_Algorithm()
			best_snake_fitness, best_snake_idx, parents_weights, parents_bias, probability = GA.parents_selection(weights, bias, fitness)
			offspring_weights, offspring_bias = GA.uniform_crossover(parents_weights, parents_bias, probability)
			offspring_weights_mutated = GA.uniform_mutation(offspring_weights)

			weights = parents_weights + offspring_weights_mutated
			bias 	= parents_bias + offspring_bias

		np.save('top_snakes_index.npy', top_snake_idx)
		print(seed)

	if show_best:
		np.random.seed(236)
		highscore 	= 0
		weights 	= None
		bias 		= None
		top_snakes = np.load('top_snakes_index2.npy')

		for generation in range(num_generations):
			start = Game(weights, bias)
			weights, bias, fitness, highscore, highscore_gen = start.run_game(highscore, (generation+1), top_snakes)

			print ('Generation: {} - Mean Fitness: {} - Max Fitness: {} - Score: {}'.format((generation+1), np.round(np.mean(fitness), 2), np.round(np.max(fitness), 2), highscore_gen))

			GA = Genetic_Algorithm()
			best_snake_fitness, best_snake_idx, parents_weights, parents_bias, probability = GA.parents_selection(weights, bias, fitness)
			offspring_weights, offspring_bias = GA.uniform_crossover(parents_weights, parents_bias, probability)
			offspring_weights_mutated = GA.uniform_mutation(offspring_weights)

			weights = parents_weights + offspring_weights_mutated
			bias 	= parents_bias + offspring_bias


#11022	Population = 1000 - Parents = 100 - Generation = 50 NO MUTATION YET - 4 direction vision (food, body, wall) - Max Score = 15 NN: [12,6,4]
#236	Population = 500 - Parents = 50 - Generation = 50 Mutation Rate: 0.05 - 4 direction vision (food, body, wall) - Max Score = 49 NN: [12,12,4]

	

