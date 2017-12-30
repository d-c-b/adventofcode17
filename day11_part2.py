with open('input_d11.txt', 'rU') as f:
  input_directions = f.readline().split(',')

direction_dict = {}

direction_dict['n'] = 0
direction_dict['ne'] = 0
direction_dict['se'] = 0
direction_dict['s'] = 0
direction_dict['sw'] = 0
direction_dict['nw'] = 0


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

def find_furthest_point_reached():
    furthest = 0
    for direction in input_directions:
        if direction == 'n':
            direction_dict['n'] += 1
        elif direction == 'ne':
            direction_dict['ne'] += 1
        elif direction == 'se':
            direction_dict['se'] += 1
        elif direction =='s':
            direction_dict['s'] += 1
        elif direction == 'sw':
            direction_dict['sw'] += 1
        elif direction == 'nw':
            direction_dict['nw'] += 1
        
        shrt_dst = shortest_distance_from_beginning()
        if shrt_dst > furthest:
            furthest = shrt_dst
        else:
            pass
    return furthest

furthest_dist = find_furthest_point_reached()
print 'Furthest instantaneous distance reached from beginning: ', furthest_dist
        