with open('input_d7.txt', 'rU') as f:
  tower_line_list = f.read().split('\n')


def find_lowest_program():
    lowest_program = tower_line_list[0].split(' ')[0]

    for line in tower_line_list:
        prog_name_weight = line.split('-> ')[0].split()
        current_program = prog_name_weight[0]

        if len(line.split('-> ')) == 2:
            dependent_progs = line.split('-> ')[1].split(', ')
            if lowest_program in dependent_progs:
                lowest_program = current_program
    return lowest_program

lowest_program = find_lowest_program()

def find_line(program):
    for i in range(len(tower_line_list)):
        prog = tower_line_list[i].split()[0]
        if prog == program:
            break
    return i


def tower_sum(line_input, weight_sum):
    try:
        branches = line_input.split('-> ')[1].split(', ')
        for branch in branches:
            br_ind = find_line(branch)
            branch_prog_weight = int(tower_line_list[br_ind].split('-> ')[0].split()[1].strip('()'))
            weight_sum += branch_prog_weight
            weight_sum = tower_sum(tower_line_list[find_line(branch)], weight_sum)
        return weight_sum
    except IndexError:
        return weight_sum
    


def find_unbalanced_branch(base_prog):
    base_branches = tower_line_list[find_line(base_prog)].split('-> ')[1].split(', ')
    branches_weights = []
    for base_branch in base_branches:
        branch_base_program_weight = int(tower_line_list[find_line(base_branch)].split('-> ')[0].split()[1].strip('()'))
        branch_weight = tower_sum(tower_line_list[find_line(base_branch)], branch_base_program_weight )
        branches_weights.append(branch_weight)
    
    for j in set(branches_weights):
        if branches_weights.count(j) == 1:
            wrong_weight_diff = ( max(set(branches_weights)) - min(set(branches_weights)) )
            global wrong_weight_diff
            return find_unbalanced_branch(base_branches[branches_weights.index(j)])
        elif len(set(branches_weights)) == 1:
            print 'Unbalanced Program: ', base_prog
            current_weight =  int(tower_line_list[find_line(base_prog)].split()[1].strip('()'))
            correct_weight = abs(current_weight - wrong_weight_diff )
            print 'Current Weight: ', current_weight
            print 'Correct Weight: ', correct_weight
            return base_prog, current_weight, correct_weight


wrong_weight_prog, curr_weight, corr_weight = find_unbalanced_branch(lowest_program)
        
    
    
    
    
    
    