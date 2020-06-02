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


	def run_game(self, highscore, highscore_gen=0, individual=1, points=0, flag=True):
		if graphics:
			pg.init()
			pg.display.set_caption('Snake Game created by T.Tran')
			#screen = pg.display.set_mode((display_width, display_height))
			clock = pg.time.Clock()
		pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, points, steps_taken, steps_left = self.restart_game()

		while flag:
			if graphics:
				clock.tick(100)
			SNAKE = Snake(pos_x, pos_y, self.weights[individual-1], self.bias[individual-1])
			snake_head, snake_list = SNAKE.draw(snake_list, snake_length, food_pos_x, food_pos_y, dx,dy)
			X = SNAKE.vision(food_pos_x, food_pos_y, snake_list)
			pos_x, pos_y, dx, dy, flag = SNAKE.move_snake(dx, dy, X, AI)
			snake_length, food_pos_x, food_pos_y, points = SNAKE.eat(snake_list, snake_length, food_pos_x, food_pos_y, points)

			if dx != 0 or dy != 0:
				steps_taken += 1
				steps_left 	-= 1

			fitscore = self.fitness_score(points, steps_taken)
			if graphics:
				self.draw_score(points, highscore, individual, steps_left, fitscore)

			if self.out_of_bound(pos_x, pos_y) or self.head_body_collision(snake_head, snake_list) or steps_left == 0:
				self.fitness.append(fitscore)

				if points > highscore:
					highscore = points
				if points > highscore_gen:
					highscore_gen = points
				if individual == num_individuals:
					break

				pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, points, steps_taken, steps_left = self.restart_game()
				individual += 1
			if graphics:
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
		fitscore = steps_taken + (2**points + 500*points**2.1) - (0.25 * steps_taken**1.3 * points**1.2)

		return (fitscore)

	def draw_score(self, points, highscore, individual, steps_left, fitscore):
		smallfont = pg.font.SysFont(None, 25)
		text_1 = smallfont.render("Score: {} Snake: {} Steps Left: {} Fitscore: {}".format(points, individual, steps_left, np.round(fitscore, 2)), True, [0,0,0])
		text_2 = smallfont.render("Highscore: {}".format(highscore), True, [0,0,0])
		screen.blit(text_1, [0,0])
		screen.blit(text_2, [display_width-120,0])

	def restart_game(self, food=True):
		pos_x 		= display_width / 2
		pos_y 		= display_height / 2

		points 		= 0
		steps_taken = 0
		steps_left 	= 200

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

		return (pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, points, steps_taken, steps_left)

if __name__ == "__main__":
	np.random.seed(0)
	highscore 	= 0
	weights 	= None
	bias 		= None

	for generation in range(num_generations):
		start = Game(weights, bias)
		weights, bias, fitness, highscore, highscore_gen = start.run_game(highscore)

		print ('Generation: {} - Mean Fitness: {} - Max Fitness: {} - Score: {}'.format((generation+1), np.round(np.mean(fitness), 2), np.round(np.max(fitness), 2), highscore_gen))

		GA = Genetic_Algorithm()
		best_snake_fitness, best_snake_idx, parents_weights, parents_bias, probability = GA.parents_selection(weights, bias, fitness)
		offspring_weights, offspring_bias = GA.uniform_crossover(parents_weights, parents_bias, probability)

		weights = parents_weights + offspring_weights
		bias 	= parents_bias + offspring_bias




	

