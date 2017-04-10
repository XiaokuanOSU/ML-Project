import sys
import random

# dataset = open("dataset.train", "r")
# lines = dataset.readlines()
# index_set = [i for i in range(0, len(lines))]
log = open("test_mutation_log.out", "w")

# train_num = int(0.8 * len(lines))
for i in range(0, 10):
	# train_output = open("data" + str(i) + ".train", "r")
	test = open("test/data" + str(i) + ".test", "r")
	lines = test.readlines()

	for j in range(1, 514):
		log.write("data" + str(i) + ".test, try attribute " + str(j) + "\n")
		malicious_modified = 0
		nonmalicious_modified = 0

		new_test = open("newtest/data" + str(i) + "_attr" + str(j) + ".test", "w")
		for line in lines:
			parts = line.split()
			target = str(j) + ":1"
			if target not in parts:
				line = line[:len(line)-2] + target + "\n"
				if parts[0] == "-1":
					malicious_modified += 1
				elif parts[0] == "+1":
					nonmalicious_modified += 1
				else:
					print (parts)
					print ("error, not starting with -1/+1")
			new_test.write(line)
		new_test.close()

		log.write("malicious modified: " + str(malicious_modified) + "\n")
		log.write("non-malicious modified: " + str(nonmalicious_modified) + "\n")

	test.close()
log.close()
