import numpy as np
input = 289326
filling_side_length = 1
#square_side_length = 1
grid =  np.zeros((3,3))
current_indices = [1,1]

grid[1][1] = 1


def surround_sum(indices):
    a = [-1, 0, 1]
    surr_sum = 0
    for i in a:
      for j in a:
        if (i==0) and (j==0):
          continue
        surr_sum += grid[indices[0]+i][indices[1]+j]

    return surr_sum


def move_right(indices):
    indices[1] += 1
    surround = surround_sum(indices)
    grid[indices[0]][indices[1]] = surround


def move_up(indices):
    indices[0] += -1
    surround = surround_sum(indices)
    grid[indices[0]][indices[1]] = surround

def move_left(indices):
    indices[1] += -1
    surround = surround_sum(indices)
    grid[indices[0]][indices[1]] = surround

def move_down(indices):
    indices[0] += 1
    surround = surround_sum(indices)
    grid[indices[0]][indices[1]] = surround

up_num = 1
lrd_num = 2

while grid[current_indices[0]][current_indices[1]] < input:


  grid = np.vstack( [np.zeros(filling_side_length+2), grid , np.zeros(filling_side_length+2)] )
  grid = np.column_stack( [  np.zeros(filling_side_length+4), grid , np.zeros(filling_side_length+4) ] )
  filling_side_length += 2
  current_indices[0] += 1
  current_indices[1] += 1

  move_right(current_indices)
  for u in range(up_num):
    if grid[current_indices[0]][current_indices[1]] >= input:
      break
    move_up(current_indices)
  up_num += 2
  for l in range(lrd_num):
    if grid[current_indices[0]][current_indices[1]] >= input:
      break
    move_left(current_indices)
  for d in range(lrd_num):
    if grid[current_indices[0]][current_indices[1]] >= input:
      break
    move_down(current_indices)
  for r in range(lrd_num):
    if grid[current_indices[0]][current_indices[1]] >= input:
      break
    move_right(current_indices)
  lrd_num += 2

print grid
print grid[current_indices[0]][current_indices[1]]
