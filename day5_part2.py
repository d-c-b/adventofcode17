# This code takes a while to run! ~ 5 mins
with open('input_d5.txt', 'rU') as f:
  jump_list = f.read().split()

count = 0
current_index = 0

while current_index in range(len(jump_list)):
  if int(jump_list[current_index]) < 3:
    jump_list[current_index] = int(jump_list[current_index]) + 1
    current_index += (int(jump_list[current_index]) - 1)

  else:
    jump_list[current_index] = int(jump_list[current_index]) - 1
    current_index += (int(jump_list[current_index]) + 1)

  count += 1

print count
