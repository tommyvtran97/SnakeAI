import numpy as np
import pygame as pg 
from settings import *
from neural_network import *
from snake import *

class Game(object):

	def __init__(self):
		pass

	def run_game(self, weights, bias, points=0, highscore=0, flag=True):
		pg.init()
		pg.display.set_caption('Snake Game created by T.Tran')
		screen = pg.display.set_mode((display_width, display_height))
		clock = pg.time.Clock()
		pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, points = self.restart_game()

		while flag:
			clock.tick(20)
			SNAKE = Snake(pos_x, pos_y, weights, bias)
			snake_head, snake_list = SNAKE.draw(screen, snake_list, snake_length, food_pos_x, food_pos_y, dx,dy)
			X = SNAKE.vision(food_pos_x, food_pos_y, snake_list)
			pos_x, pos_y, dx, dy, flag = SNAKE.move_player(dx, dy, X)
			snake_length, food_pos_x, food_pos_y, points = SNAKE.eat(screen, snake_list, snake_length, food_pos_x, food_pos_y, points)
			self.draw_score(screen, points, highscore)

			if self.out_of_bound(pos_x, pos_y) or self.head_body_collision(snake_head, snake_list):
				if points > highscore:
					highscore = points

				pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, points = self.restart_game()

			weights = SNAKE.weights
			bias = SNAKE.bias
				
			pg.display.update()

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

	def draw_score(self, screen, points, highscore):
		smallfont = pg.font.SysFont(None, 25)
		text_1 = smallfont.render("Score: {}".format(points), True, [0,0,0])
		text_2 = smallfont.render("Highscore: {}".format(highscore), True, [0,0,0])
		screen.blit(text_1, [0,0])
		screen.blit(text_2, [400,0])


	def restart_game(self, food=True):
		pos_x 	= display_width / 2
		pos_y 	= display_height / 2
		points 	= 0

		dx 		= 0
		dy 		= 0

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

		return (pos_x, pos_y, food_pos_x, food_pos_y, dx, dy, snake_list, snake_length, points)

if __name__ == "__main__":
	np.random.seed(0)
	weights = None
	bias = None

	start = Game()
	start.run_game(weights, bias)

