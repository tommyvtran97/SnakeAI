"""

This script is used to generate the plots for
the analysis of the performance by changing the
grid size of the environment

"""

import matplotlib.pyplot as plt

path = 'Saved/Performance_Data/'
savepath = 'Saved/Model_7462/Images/' 
save = 1

file1 = open(path + 'performance_10x10.txt', 'r')
file2 = open(path + 'performance_15x15.txt', 'r')
file3 = open(path + 'performance_20x20.txt', 'r')
file4 = open(path + 'performance_25x25.txt', 'r')

lines1 = file1.readlines()
lines2 = file2.readlines()
lines3 = file3.readlines()
lines4 = file4.readlines()

snake				= []
score_normalized1 	= []
score_normalized2 	= []
score_normalized3 	= []
score_normalized4 	= []

for line in lines1:
	data = line.strip('\n').split(',')
	snake.append(int(data[0]))
	score_normalized1.append(int(data[1])/(10*10))

for line in lines2:
	data = line.strip('\n').split(',')
	score_normalized2.append(int(data[1])/(15*15))
	
for line in lines3:
	data = line.strip('\n').split(',')
	score_normalized3.append(int(data[1])/(20*20))

for line in lines4:
	data = line.strip('\n').split(',')
	score_normalized4.append(int(data[1])/(25*25))

plt.plot(snake, score_normalized1, label='10x10 grid')
plt.plot(snake, score_normalized2, label='15x15 grid')
plt.plot(snake, score_normalized3, label='20x20 grid')
plt.plot(snake, score_normalized4, label='25x25 grid')
plt.xlabel('Number of runs [-]')
plt.ylabel('Maximum score normalized [-]')
plt.grid()
plt.legend(loc=2)

if save:
	plt.savefig(savepath + 'sensitivity3.png', dpi=600)
	
plt.show()
	