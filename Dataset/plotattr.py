import sys
import random
import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

filename = "newtestresult/log"
filehandle = open(filename,'r')
lines = filehandle.readlines()
filehandle.close()

addarr = []
l = len(lines)
for i in range(1,int(l/2),2):
	linenow = lines[i]
	sep = linenow.split()
	num = float(sep[2][:-1])
	addarr.append(num)
	#print (num)

subarr = []
l = len(lines)
for i in range(int(l/2)+1,l,2):
	linenow = lines[i]
	sep = linenow.split()
	num = float(sep[2][:-1])
	subarr.append(num)
	#print (num)

#print (len(addarr),len(subarr))

#plot
x = [i for i in range(0,len(addarr))]
output = "addattr.eps"
plt.plot(x,addarr,label = "attribute: 0-->1", color = "blue")
plt.legend()
plt.xlabel('Number of modified TOP attributes')
plt.ylabel('Accuracy (%)')
plt.savefig(output, format='eps', dpi=300)

x = [i for i in range(0,len(subarr))]
output = "bothattr.eps"
plt.plot(x,subarr,label = "attribute: 1-->0", color = "red")
plt.legend()
plt.savefig(output, format='eps', dpi=300)

plt.clf()
x = [i for i in range(0,len(subarr))]
output = "subattr.eps"
plt.plot(x,subarr,label = "attribute: 1-->0", color = "red")
plt.legend()
plt.xlabel('Number of modified TOP attributes')
plt.ylabel('Accuracy (%)')
plt.savefig(output, format='eps', dpi=300)


#changing single attr
plt.clf()
x = [i for i in range(0,531)]
y = [98.6667 for i in range(0,531)]
output = "singleattr.eps"
plt.plot(x,y,label = "attribute: 0-->1", color = "blue")
plt.legend()
plt.ylim(90, 100)
plt.xlabel('index of attribute')
plt.ylabel('Accuracy (%)')
plt.savefig(output, format='eps', dpi=300)

filename = "test/data0.test"
filehandle = open(filename,"r")
lines = filehandle.readlines()
filehandle.close()

poscount = 0
negcount = 0
for line in lines:
	sep = line.split()
	num = int(sep[0])
	if num == 1:
		poscount += 1
	else:
		negcount += 1

print ("+1:",poscount,"-1:",negcount)


















