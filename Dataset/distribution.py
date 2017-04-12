import sys
import random
import string
import numpy as np

filename = sys.argv[1]
printnum = int(sys.argv[2])
filehandle = open(filename,"r")
lines = filehandle.readlines()
filehandle.close()

countpos = 0
countneg = 0
posarr = np.zeros((540,), )
negarr = np.zeros((540,), )
for line in lines:
	sep = line.split()
	lbl = int(sep[0])
	if lbl == 1:
		countpos += 1
	else:
		countneg += 1

	for item in sep[1:]:
		idx = int(item.split(":")[0])
		if lbl == 1:
			posarr[idx] += 1			
		else:
			negarr[idx] += 1

np.set_printoptions(precision=3)

diffarr = posarr/countpos-negarr/countneg
idxarr = [i for i in range(0,540)]
sortedidx  =  np.array([idx for (diff,idx) in sorted(zip(diffarr,idxarr), reverse=True, key=lambda pair: pair[0])])
sorteddiff = np.array([diff for (diff,idx) in sorted(zip(diffarr,idxarr), reverse=True, key=lambda pair: pair[0])])

#print (sorteddiff[0:printnum])
print (sortedidx[0:printnum])

outputfilename = filename.split(".")[0] + ".addattr" + str(printnum)
print (outputfilename)
filehandle = open(outputfilename,"w+")
for item in sortedidx[0:printnum]:
	filehandle.write(str(item)+"\n")
filehandle.close()

sortedidx  =  np.array([idx for (diff,idx) in sorted(zip(diffarr,idxarr), key=lambda pair: pair[0])])
sorteddiff = np.array([diff for (diff,idx) in sorted(zip(diffarr,idxarr), key=lambda pair: pair[0])])

outputfilename = filename.split(".")[0] + ".subattr" + str(printnum)
print (outputfilename)
filehandle = open(outputfilename,"w+")
for item in sortedidx[0:printnum]:
	filehandle.write(str(item)+"\n")
filehandle.close()









