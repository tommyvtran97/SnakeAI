# Snake Game Artificial Intelligence using a Genetic Algorithm

The AI agent is trained using a feed forward neural network in combination with a genetic algorithm. The feed forward neural network consists of 24 inputs. The inputs are based on the vision of the snake. The snake can look in 8 directions and in each directions it has three inputs, the food, body and wall (3x8). The input for the food is binary whereas for the body and the wall the distance relative to the head of the snake is calculated. One hidden layer with 16 neurons and an output layer with 4 outputs (left, right, up and down) which indicate the direction to be taken by the snake in the next state. 

For the genetic algorithm, uniform crossover and uniform mutation are used. Furthermore training is done using a population size of 500 snakes and a mutation rate of 0.01 (1%).

## Part 1) Requirements
The packages used in this progam are listed below. If you already have these packages installed, then no actions are required and the program should run properly. If this is not the case run the following command `pip install -r requirements.txt`

* Pygame
* Numpy
* Matplotlib

## Part 2) Settings 
There are three combinations of settings that can be used. The first option is to train the snakes. Note that `graphics_training` is turned off as it speeds up the training process. However, if you want to see the snakes progress over time during training this can be turned on. Note that document already consist of a pre-trained model. Only use this option if you want to create a new model.  

* graphics_training=0
* AI=1
* train=1
* show_best=0
* best_snake=0
* best_snake_graphics=0
* best_snake_runs=1

The second option is to show the best performing snakes of each generations from training.

* graphics_training=0
* AI=1
* train=0
* show_best=1
* best_snake=0
* best_snake_graphics=0
* best_snake_runs=1
 
 The third option is to show the best performing snake from training. Note that `best_snake_runs` is by default 1. However, if you want to let the best performing snake play for multiple times change this accordingly.
 
* graphics_training=0
* AI=1
* train=0
* show_best=0
* best_snake=1
* best_snake_graphics=1
* best_snake_runs=1

## Part 3) Run the game
After intialization the settings, the game can be started by navigation to the main folder and running the following command: `python game.py`
