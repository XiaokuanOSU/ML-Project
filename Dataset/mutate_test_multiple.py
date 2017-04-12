#usage: python mutate_test_multiple.py {0 (remove) or 1 (add)} data0.attrlist data0.test data0.new.test
import sys
import random

mode = int(sys.argv[1])
# dataset = open("dataset.train", "r")
# lines = dataset.readlines()
# index_set = [i for i in range(0, len(lines))]
input_attr = []
filename = sys.argv[2]
input_file = open(filename, "r")
lines = input_file.readlines()
for line in lines:
	input_attr.append(int(line))
# print input_index_max

input_attr = sorted(input_attr)
print (input_attr)
# train_num = int(0.8 * len(lines))

if mode == 1:
	# train_output = open("data" + str(i) + ".train", "r")
	test = open(sys.argv[3], "r")
	lines = test.readlines()
	new_test = open(sys.argv[4], "w+")

	for line in lines:
		# print input_attr
		parts = line.split()
		temp_line = parts[0]
		
		j = 1
		k = 0
		while j < len(parts) and k < len(input_attr):
			attribute = int(parts[j].split(":")[0])
			if attribute < input_attr[k]:
				temp_line = temp_line + " " + parts[j]
				j += 1
			elif attribute == input_attr[k]:
				temp_line = temp_line + " " + parts[j]
				j += 1
				k += 1
			else:
				temp_line = temp_line + " " + str(input_attr[k]) + ":1"
				k += 1

		for m in range(j, len(parts)):
			temp_line = temp_line + " " + parts[m]
		for m in range(k, len(input_attr)):
			temp_line = temp_line + " " + str(input_attr[m]) + ":1"

		temp_line = temp_line + "\n"
		new_test.write(temp_line)
		#print (temp_line)

	new_test.close()
	test.close()

elif mode == 0:
	# train_output = open("data" + str(i) + ".train", "r")
	test = open(sys.argv[3], "r")
	lines = test.readlines()
	new_test = open(sys.argv[4], "w+")

	for line in lines:
		parts = line.split()
		# temp_line = line
		for attribute in input_attr:
			target = str(attribute) + ":1"
			if target in parts:
				parts.remove(target)
		#temp_line = parts[0]
		temp_line = ""
		for part in parts:
			temp_line = temp_line + " " + part
		temp_line = temp_line + "\n"
		new_test.write(temp_line)
		#print (temp_line)

	new_test.close()
	test.close()

else:
	print ("wrong input!")
