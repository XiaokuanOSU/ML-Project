import sys
import random

dataset = open("dataset.train", "r")
lines = dataset.readlines()
index_set = [i for i in range(0, len(lines))]

train_num = int(0.8 * len(lines))
for i in range(0, 10):
	train_output = open("train/data" + str(i) + ".train", "w")
	test_output = open("test/data" + str(i) + ".test", "w")

	random.shuffle(index_set)
	print (i)
	print (index_set)
	for j in range(0, train_num):
		line = lines[index_set[j]]
		line = line[:len(line)-4] # remove "  -1"
		train_output.write(line+"\n")
	for j in range(train_num, len(lines)):
		line = lines[index_set[j]]
		line = line[:len(line)-4] # remove "  -1"
		test_output.write(line+"\n")

	train_output.close()
	test_output.close()

dataset.close()
