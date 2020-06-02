import pygame as pg 
"""

This script contains the main settings used for the Snake Game and the 
implementation of the Neural Network using an Evolutionary Approach, by
applying an genetic algorithm using crossover and mutation. The settings
can be changed to the preference of the user.

"""

# Program Settings
graphics_training 	= 0
AI 					= 1
train				= 0
show_best			= 1

# Snake Game Setttings
display_width 		= 520
display_height		= 520
offset 				= 20

snake_size			= 20
snake_length		= 3

# Neural Network Settings
layer 				= [12,12,4]
weights_size 		= 192
bias_size	 		= 16

# Genetic Algorithm Settings
num_individuals 	= 500
num_parents			= 50
num_generations		= 50
num_offspring 		= num_individuals - num_parents
mutation_rate		= 0.05

if show_best or graphics_training:
	screen = pg.display.set_mode((display_width, display_height))



