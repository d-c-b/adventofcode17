import numpy as np
checksum = 0
f = open('input_d2.txt', 'r')

lines = np.loadtxt(f)

pairs = []
for line in lines:
  diff = max(line) - min(line)
  checksum += diff

# part 1 to return the checksum
print checksum
