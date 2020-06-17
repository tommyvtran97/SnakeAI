"""

This script is used to generate the plots for
the sensitivity analysis of the algorithm

"""


import matplotlib.pyplot as plt

path  		= 'Saved/Performance_Data/'
savepath 	= 'Saved/Model_7462/Images/' 
save  		= 0

file1 = open(path + 'training_data_500_0.01.txt', 'r')
file2 = open(path + 'training_data_500_0.02.txt', 'r')
file3 = open(path + 'training_data_500_0.03.txt', 'r')
file4 = open(path + 'training_data_500_0.04.txt', 'r')
file5 = open(path + 'training_data_500_0.05.txt', 'r')

file6 = open(path + 'training_data_100_0.01.txt', 'r')
file7 = open(path + 'training_data_200_0.01.txt', 'r')
file8 = open(path + 'training_data_300_0.01.txt', 'r')
file9 = open(path + 'training_data_400_0.01.txt', 'r')

lines1  = file1.readlines()
lines2  = file2.readlines()
lines3  = file3.readlines()
lines4  = file4.readlines()
lines5  = file5.readlines()
lines6  = file6.readlines()
lines7  = file7.readlines()
lines8  = file8.readlines()
lines9  = file9.readlines()

generation = []

mean_fitness1 = []
mean_fitness2 = []
mean_fitness3 = []
mean_fitness4 = []
mean_fitness5 = []
mean_fitness6 = []
mean_fitness7 = []
mean_fitness8 = []
mean_fitness9 = []

max_fitness1 = []
max_fitness2 = []
max_fitness3 = []
max_fitness4 = []
max_fitness5 = []
max_fitness6 = []
max_fitness7 = []
max_fitness8 = []
max_fitness9 = []

max_score1 = []
max_score2 = []
max_score3 = []
max_score4 = []
max_score5 = []
max_score6 = []
max_score7 = []
max_score8 = []
max_score9 = []

for line in lines1:
	data = line.strip('\n').split(',')
	generation.append(int(data[0]))
	mean_fitness1.append(float(data[1]))
	max_fitness1.append(float(data[2]))
	max_score1.append(int(data[3]))
for line in lines2:
	data = line.strip('\n').split(',')
	mean_fitness2.append(float(data[1]))
	max_fitness2.append(float(data[2]))
	max_score2.append(int(data[3]))
for line in lines3:
	data = line.strip('\n').split(',')
	mean_fitness3.append(float(data[1]))
	max_fitness3.append(float(data[2]))
	max_score3.append(int(data[3]))
for line in lines4:
	data = line.strip('\n').split(',')
	mean_fitness4.append(float(data[1]))
	max_fitness4.append(float(data[2]))
	max_score4.append(int(data[3]))
for line in lines5:
	data = line.strip('\n').split(',')
	mean_fitness5.append(float(data[1]))
	max_fitness5.append(float(data[2]))
	max_score5.append(int(data[3]))
for line in lines6:
	data = line.strip('\n').split(',')
	mean_fitness6.append(float(data[1]))
	max_fitness6.append(float(data[2]))
	max_score6.append(int(data[3]))
for line in lines7:
	data = line.strip('\n').split(',')
	mean_fitness7.append(float(data[1]))
	max_fitness7.append(float(data[2]))
	max_score7.append(int(data[3]))
for line in lines8:
	data = line.strip('\n').split(',')
	mean_fitness8.append(float(data[1]))
	max_fitness8.append(float(data[2]))
	max_score8.append(int(data[3]))
for line in lines9:
	data = line.strip('\n').split(',')
	mean_fitness9.append(float(data[1]))
	max_fitness9.append(float(data[2]))
	max_score9.append(int(data[3]))

list1 = [0.8, 0.8, 0.72, 0.4, 0.36]
list2 = [0.8, 0.68, 0.48, 0.48, 0.48]
list3 = [0.56, 0.76, 0.6, 0.48, 0.44]
list4 = [0.64, 0.64, 0.56, 0.6, 0.36]
list5 = [0.48, 0.44, 0.44, 0.4, 0.28]

mutation_rate = [0.01, 0.02, 0.03, 0.04, 0.05]

plt.plot(mutation_rate, list1, '-^', label='Population Size: 500')
plt.plot(mutation_rate, list2, '-^', label='Population Size: 400')
plt.plot(mutation_rate, list3, '-^', label='Population Size: 300')
plt.plot(mutation_rate, list4, '-^', label='Population Size: 200')
plt.plot(mutation_rate, list5, '-^', label='Population Size: 100')

plt.xlabel('Mutation rate [-]')
plt.ylabel('Success rate [-]')
plt.legend(loc=0)
plt.grid()

if save:
	plt.savefig(savepath + 'sensitivity.png', dpi=600)

fig1 = plt.figure(figsize=(15,6))
plt.subplot(311)
plt.plot(generation, max_fitness1, label='Mutation rate: 0.01')
plt.plot(generation, max_fitness2, label='Mutation rate: 0.02')
plt.plot(generation, max_fitness3, label='Mutation rate: 0.03')
plt.plot(generation, max_fitness4, label='Mutation rate: 0.04')
plt.plot(generation, max_fitness5, label='Mutation rate: 0.05')
plt.yscale('log')
plt.ylabel('Maxmimum fitness [-]')
plt.grid()
plt.legend(loc=2)

plt.subplot(312)
plt.plot(generation, mean_fitness1)
plt.plot(generation, mean_fitness2)
plt.plot(generation, mean_fitness3)
plt.plot(generation, mean_fitness4)
plt.plot(generation, mean_fitness5)
plt.yscale('log')
plt.ylabel('Mean fitness [-]')
plt.grid()

plt.subplot(313)
plt.plot(generation, max_score1)
plt.plot(generation, max_score2)
plt.plot(generation, max_score3)
plt.plot(generation, max_score4)
plt.plot(generation, max_score5)
plt.xlabel('Generation [-]')
plt.ylabel('Score [-]')
plt.grid()

fig1.align_labels()

if save:
	plt.savefig(savepath + 'sensitivity1.png', dpi=600)

fig2 = plt.figure(figsize=(15,6))
plt.subplot(311)
plt.plot(generation, max_fitness6, label='Population size: 100')
plt.plot(generation, max_fitness7, label='Population size: 200')
plt.plot(generation, max_fitness8, label='Population size: 300')
plt.plot(generation, max_fitness9, label='Population size: 400')
plt.plot(generation, max_fitness1, label='Population size: 500')
plt.yscale('log')
plt.ylabel('Maximum fitness [-]')
plt.grid()
plt.legend(loc=2)

plt.subplot(312)
plt.plot(generation, mean_fitness5)
plt.plot(generation, mean_fitness6)
plt.plot(generation, mean_fitness7)
plt.plot(generation, mean_fitness8)
plt.plot(generation, mean_fitness1)
plt.yscale('log')
plt.ylabel('Mean fitness [-]')
plt.grid()

plt.subplot(313)
plt.plot(generation, max_score5)
plt.plot(generation, max_score6)
plt.plot(generation, max_score7)
plt.plot(generation, max_score8)
plt.plot(generation, max_score1)
plt.xlabel('Generation [-]')
plt.ylabel('Score [-]')
plt.grid()

fig2.align_labels()

if save:
	plt.savefig(savepath + 'sensitivity2.png', dpi=600)

plt.show()
