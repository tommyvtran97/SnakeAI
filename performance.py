import numpy as np
import matplotlib.pyplot as plt 

save 	= 0

path 	= 'Saved/Snake_8Vision_149/'
file1 	= open(path + 'top_snake_performance.txt', 'r')
file2 	= open(path + 'training_data.txt', 'r')

lines1 	= file1.readlines()
lines2 	= file2.readlines()

snake 	= []
score 	= []

generation 		= []
mean_fitness 	= []
max_fitness 	= []
max_score 		= []


for line in lines1:
	data = line.strip('\n').split(',')
	snake.append(int(data[0]))
	score.append(int(data[1]))

for line in lines2:
	data = line.strip('\n').split(',')
	generation.append(float(data[0]))
	mean_fitness.append(float(data[1]))
	max_fitness.append(float(data[2]))
	max_score.append(float(data[3]))


plt.plot(snake, score, label='Maximum score')
plt.plot([snake[0], snake[-1]], [np.mean(score), np.mean(score)], label='Mean')
plt.xlabel('Number of runs')
plt.ylabel('Score')
plt.legend(loc=2)
plt.grid()

if save:
	plt.savefig(path + 'performance.png', dpi=600)

fig = plt.figure(figsize=(10,6))
plt.subplot(311)
plt.plot(generation, max_fitness, label='Maximum Fitness')
plt.ylabel('Fitness')
plt.grid()
plt.legend(loc=2)

plt.subplot(312)
plt.plot(generation, mean_fitness, label='Mean Fitness')
plt.ylabel('Fitness')
plt.grid()
plt.legend(loc=2)

plt.subplot(313)
plt.plot(generation, max_score, label='Maximum Score')
plt.xlabel('Generation')
plt.ylabel('Score')
plt.grid()
plt.legend(loc=2)

fig.align_labels()

if save:
	plt.savefig(path + 'training.png', dpi=600)

plt.show()

