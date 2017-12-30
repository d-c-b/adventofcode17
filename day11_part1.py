with open('input_d11.txt', 'rU') as f:
  input_directions = f.readline().split(',')

direction_dict = {}

direction_dict['n'] = input_directions.count('n')
direction_dict['ne'] = input_directions.count('ne')
direction_dict['se'] = input_directions.count('se')
direction_dict['s'] = input_directions.count('s')
direction_dict['sw'] = input_directions.count('sw')
direction_dict['nw'] = input_directions.count('nw')



print 'Initial configuration of directions: ', direction_dict

def cancel_opposite_directions(dir_1, dir_2):
    
    if direction_dict[dir_1] > direction_dict[dir_2]:
        direction_dict[dir_1] -= direction_dict[dir_2]
        direction_dict[dir_2] = 0


    elif direction_dict[dir_2] > direction_dict[dir_1]:
        direction_dict[dir_2] -= direction_dict[dir_1]
        direction_dict[dir_1] = 0

    elif direction_dict[dir_2] == direction_dict[dir_1]:
        direction_dict[dir_1] = 0
        direction_dict[dir_2] = 0


def combine_diagonal_directions(dir_1, dir_2, resultant_dir):
    
    if direction_dict[dir_1] > direction_dict[dir_2]:
        direction_dict[resultant_dir] += direction_dict[dir_2]
        direction_dict[dir_1] -= direction_dict[dir_2]
        direction_dict[dir_2] = 0
        

    elif direction_dict[dir_2] > direction_dict[dir_1]:
        direction_dict[resultant_dir] += direction_dict[dir_1]
        direction_dict[dir_2] -= direction_dict[dir_1]
        direction_dict[dir_1] = 0
        
    elif direction_dict[dir_2] == direction_dict[dir_1]:
        direction_dict[resultant_dir] += direction_dict[dir_2]
        direction_dict[dir_1] = 0
        direction_dict[dir_2] = 0


def shortest_distance_from_beginning():
    
    cancel_opposite_directions('n', 's')
    cancel_opposite_directions('ne', 'sw')
    cancel_opposite_directions('nw', 'se')
    
    combine_diagonal_directions('ne','nw','n')
    combine_diagonal_directions('se','sw','s')
    combine_diagonal_directions('n','se','ne')
    combine_diagonal_directions('ne','s','se')
    combine_diagonal_directions('nw','s','sw')
    combine_diagonal_directions('n','sw','nw')

    return sum(direction_dict.values())

short_dist = shortest_distance_from_beginning()

print 'Equivalent to:     ', direction_dict

print 'Shortest path to same end point:  ', short_dist