with open('input_d7.txt', 'r') as f:
  tower_line_list = f.read().split('\r\n')

lowest_program = tower_line_list[0].split(' ')[0]

for line in tower_line_list:
  prog_name_weight = line.split('-> ')[0].split(' ')
  current_program = prog_name_weight[0]

  if len(line.split('-> ')) == 2:
    dependent_progs = line.split('-> ')[1].split(', ')
    if lowest_program in dependent_progs:
      lowest_program = current_program

print lowest_program
