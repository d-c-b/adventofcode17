import numpy as np
checksum = 0
f = open('input_d2.txt', 'r')

lines = np.loadtxt(f)

pairs = []
for line in lines:
  diff = max(line) - min(line)
  checksum += diff



for line in lines:
  for i in range(len(line)):
    for j in range(i, len(line)):
      if (i != j) & (int(line[i]) % int(line[j]) == 0):
        pairs.append([line[i],line[j]])
      elif (i != j) &  (int(line[j]) % int(line[i]) == 0):
        pairs.append([line[j],line[i]])

checkdiv = 0
for pair in pairs:
  div = int(pair[0]/pair[1])
  checkdiv += div

# part 2 to return the division of two numbers in a row where modulo division is zero
print checkdiv
