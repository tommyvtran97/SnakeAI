"""

This script contains the main settings used for the Snake Game and the 
implementation of the Neural Network using an Evolutionary Approach, by
applying an genetic algorithm using crossover and mutation. The settings
can be changed to the preference of the user.

"""

# Program Settings
graphics 			= 0
AI 					= 1

# Snake Game Setttings
display_width 		= 520
display_height		= 520
offset 				= 20

snake_size			= 20
snake_length		= 3

# Neural Network Settings
layer 				= [12,6,4]
weights_size 		= 96
bias_size	 		= 10

# Genetic Algorithm Settings
num_individuals 	= 50
num_parents			= 5
num_generations		= 10
num_offspring 		= num_individuals - num_parents

if graphics:
	screen = pg.display.set_mode((display_width, display_height))



