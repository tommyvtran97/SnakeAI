"""

This script contains functions for the snake. These
functions are used together with the Snake Game
to create a working environment. 

"""

import numpy as np 
import pygame as pg 
from math import *
from settings import *
from neural_network import*

class Snake(object):

	def __init__(self, pos_x, pos_y, weights, bias, show_best=False):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.NN = Neural_Network(weights, bias)

	def vision(self, food_pos_x, food_pos_y, snake_list):			
		food1 = food2 = food3 = food4 = food5 = food6 = food7 = food8 = 0
		body1 = body2 = body3 = body4 = body5 = body6 = body7 = body8 = 0

		if (self.pos_x - food_pos_x) != 0 and (self.pos_y - food_pos_y) != 0:
			angle_food = np.degrees(atan((self.pos_y - food_pos_y) / (self.pos_x - food_pos_x)))
		else:
			angle_food = False

		if self.pos_x == food_pos_x and self.pos_y > food_pos_y:
			food1 = 1
		if self.pos_x < food_pos_x and angle_food == -45:
			food2 = 1
		if self.pos_x < food_pos_x and self.pos_y == food_pos_y:
			food3 = 1
		if self.pos_x < food_pos_x and angle_food == 45:
			food4 = 1
		if self.pos_x == food_pos_x and self.pos_y < food_pos_y:
			food5 = 1
		if self.pos_x > food_pos_x and angle_food == -45:
			food6 = 1
		if self.pos_x > food_pos_x and self.pos_y == food_pos_y:
			food7 = 1
		if self.pos_x > food_pos_x and angle_food == 45:
			food8 = 1

		for x in snake_list[:-1]:
			if (self.pos_x - x[0]) != 0 and (self.pos_y - x[1]) != 0:
				body_angle = np.degrees(atan((self.pos_y - x[1]) / (self.pos_x - x[0])))
			else:
				body_angle = False

			if self.pos_x == x[0] and self.pos_y > x[1]:
				body1 = 1 / (abs(self.pos_y - x[1]) / (snake_size))
			if self.pos_x < x[0] and body_angle == -45:
				body2 = 1 / ((np.sqrt((self.pos_x - x[0])**2 + (self.pos_y - x[1])**2)) / (np.sqrt(2*snake_size**2)))
			if self.pos_x < x[0] and self.pos_y == x[1]:
				body3 = 1 / (abs(self.pos_x - x[0]) / (snake_size))
			if self.pos_x < x[0] and body_angle == 45:
				body4 = 1 / ((np.sqrt((self.pos_x - x[0])**2 + (self.pos_y - x[1])**2)) / (np.sqrt(2*snake_size**2)))
			if self.pos_x == x[0] and self.pos_y < x[1]:
				body5 = 1 / (abs(self.pos_y - x[1]) / (snake_size))
			if self.pos_x > x[0] and body_angle == -45:
				body6 = 1 / ((np.sqrt((self.pos_x - x[0])**2 + (self.pos_y - x[1])**2)) / (np.sqrt(2*snake_size**2)))
			if self.pos_x > x[0] and self.pos_y == x[1]:
				body7 = 1 / (abs(self.pos_x - x[0]) / (snake_size))
			if self.pos_x > x[0] and body_angle == 45:
				body8 = 1 / ((np.sqrt((self.pos_x - x[0])**2 + (self.pos_y - x[1])**2)) / (np.sqrt(2*snake_size**2)))

		wall1 = 1 / (abs((self.pos_y - offset) + snake_size) / (snake_size))
		if ((display_width - snake_size) - self.pos_x) < (self.pos_y - offset):
			wall2 = 1 / ((np.sqrt(2*(display_width - self.pos_x)**2)) / (np.sqrt(2*snake_size**2)))
		else:
			wall2 = 1 / ((np.sqrt(2*(self.pos_y - offset + snake_size)**2)) / (np.sqrt(2*snake_size**2)))
		wall3 = 1 / (abs(display_width - self.pos_x) / (snake_size))
		if ((display_width - snake_size) - self.pos_x) < ((display_height - snake_size) - self.pos_y):
			wall4 = 1 / ((np.sqrt(2*(display_width - self.pos_x)**2)) / (np.sqrt(2*snake_size**2)))
		else:
			wall4 = 1 / ((np.sqrt(2*(display_height - self.pos_y)**2)) / (np.sqrt(2*snake_size**2)))
		wall5 = 1 / (abs(display_height - self.pos_y) / (snake_size))
		if (self.pos_x) < ((display_height - snake_size) - self.pos_y):
			wall6 = 1 / ((np.sqrt(2*(self.pos_x + snake_size)**2)) / (np.sqrt(2*snake_size**2)))
		else:
			wall6 = 1 / ((np.sqrt(2*(display_height - self.pos_y)**2)) / (np.sqrt(2*snake_size**2)))
		wall7 = 1 / (abs(self.pos_x + snake_size) / (snake_size))
		if (self.pos_x) < (self.pos_y - offset):
			wall8 = 1 / ((np.sqrt(2*(self.pos_x + snake_size)**2)) / (np.sqrt(2*snake_size**2)))
		else:
			wall8 = 1 / ((np.sqrt(2*(self.pos_y - offset + snake_size)**2)) / (np.sqrt(2*snake_size**2)))

		X = np.array([food1, food2, food3, food4, food5, food6, food7, food8, body1, body2, body3, body4,  body5, body6, body7, body8,\
				      wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8])
	
		return (X)

	def move_snake(self, dx, dy, X, AI=False, flag=True):
		output = self.NN.feed_forward(X)

		if AI:
				if output == 0:
					dx = -snake_size
					dy = 0
				if output == 1:
					dx = snake_size
					dy = 0
				if output == 2:
					dx = 0
					dy = -snake_size
				if output == 3:
					dx = 0
					dy = snake_size
				if graphics_training or show_best or best_snake_graphics:
					for event in pg.event.get():
						if event.type == pg.QUIT:
							flag = False

		if not AI:
			dx = dy = 0
			for event in pg.event.get():
				if event.type == pg.QUIT:
					flag = False
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_LEFT:
						dx = -snake_size
						dy = 0
					if event.key == pg.K_RIGHT:
						dx = snake_size
						dy = 0
					if event.key == pg.K_UP:
						dx = 0
						dy = -snake_size
					if event.key == pg.K_DOWN:
						dx = 0
						dy = snake_size

		self.pos_x += dx
		self.pos_y += dy

		return (self.pos_x, self.pos_y, dx, dy, flag)

	def eat(self, snake_list, snake_length, food_pos_x, food_pos_y, points, steps_left, food=True):
		if self.pos_x == food_pos_x and self.pos_y == food_pos_y:
			while food:
				food_pos_x = np.random.choice(np.arange(0, display_width, step=snake_size))
				food_pos_y = np.random.choice(np.arange(offset, display_height, step=snake_size))
				for x in snake_list:
					if x[0] == food_pos_x and x[1] == food_pos_y:
						food = True
						break
					else:
						food = False
			if graphics_training or show_best or best_snake_graphics:
				pg.draw.rect(screen, [255,255,255], [food_pos_x, food_pos_y, snake_size, snake_size])
				pg.draw.rect(screen, [255, 0, 0], [food_pos_x+3, food_pos_y+3, snake_size-6, snake_size-6])

			snake_length += 1
			points		 += 1
			steps_left 	 += 100

		return (snake_length, food_pos_x, food_pos_y, points, steps_left)

	def draw(self, snake_list, snake_length, food_pos_x, food_pos_y, dx, dy):
		snake_head = [self.pos_x, self.pos_y]
		if dx != 0 or dy != 0:
			snake_list.append(snake_head)

		if len(snake_list) > snake_length:
			del snake_list[0]
		if graphics_training or show_best or best_snake_graphics:
			screen.fill([0,0,0])
			pg.draw.rect(screen, [255,255,255], [0, 0, display_width, offset])
			pg.draw.rect(screen, [255,255,255], [food_pos_x, food_pos_y, snake_size, snake_size])
			pg.draw.rect(screen, [255, 0, 0], [food_pos_x+3, food_pos_y+3, snake_size-6, snake_size-6])

			for x in snake_list:
				if x == snake_list[-1]:
					pg.draw.rect(screen, [255,255,255], [x[0], x[1], snake_size, snake_size])
					pg.draw.rect(screen, [0,0,255], [x[0]+3, x[1]+3, snake_size-6, snake_size-6])
				else:
					pg.draw.rect(screen, [255,255,255], [x[0], x[1], snake_size, snake_size])
					pg.draw.rect(screen, [0,255,0], [x[0]+3, x[1]+3, snake_size-6, snake_size-6])

		return (snake_head, snake_list)


