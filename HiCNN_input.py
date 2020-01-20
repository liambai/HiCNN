import numpy as np
import sys
import math


# input size
sizeIn = 40
# output size
sizeOut = 28
# resolution
res = 10000

submats = []
index = []

# contact matrix 
f_in = sys.argv[1]
# chromosome length
chr_len = sys.argv[2]
# concatenated submatrices
f_out1 = sys.argv[3]
# indexes for submatrices
f_out2 = sys.argv[4]

bins = math.ceil(chr_len / res)
HiCMat = np.loadtxt(f_in)

maxIndex = (2000000 / res) + 1

for i in range(0, bins, sizeOut):
	for j in range(i, bins, sizeOut):
		if (abs(i-j) > maxIndex or i + sizeIn >= bins or j + sizeIn >= bins):
			continue
		submat = HiCMat[i:i+sizeIn, j:j+sizeIN]
		submats.append([submat,])
			a = i + 6
			b = j + 6
			index.append((a, b))

index = np.array(index)
submats = np.array(submats)
submats = submats.astype(np.float32)
np.save(f_out1, submats)
np.save(f_out2, index)


