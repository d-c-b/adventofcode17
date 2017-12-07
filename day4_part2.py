import numpy as np

with open('input_d4.txt', 'r') as f:
  passwords = f.read().split('\r\n')

invalid_passwords = 0

print 'Total number of different passwords: ', len(passwords)

for password in passwords:
  words = password.split(' ')
  continue_checking = True
  for i in range(len(words)):
    if continue_checking == True:
      for j in range(len(words)):
        if (sorted(words[i]) == sorted(words[j]) and i != j):
          continue_checking = False
          invalid_passwords += 1
          break
        else:
          continue
    else:
      break

print 'Number of Invalid Passwords: ', invalid_passwords

valid_passwords = len(passwords) - invalid_passwords
print 'Number of Valid Passwords: ', valid_passwords
