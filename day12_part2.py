with open('input_d12.txt', 'rU') as f:
  pipe_connections = f.read().split('\n')

groups = []

def find_connected_progs(prg_num):
    connections = map(int, pipe_connections[prg_num].split(' <-> ')[-1].split(', '))

    for connection in connections:
        already_done = connection in group_prgs
        if already_done == False:
            group_prgs.append(connection)
            find_connected_progs(connection)


def program_already_grouped(prg_num):
    grouped_progs = [prog for group in groups for prog in group]
    return prg_num in grouped_progs

prog_nums = range(len(pipe_connections))

group_prgs = []
for i in prog_nums:
    if program_already_grouped(i) == False:
        find_connected_progs(i)
        groups.append(group_prgs)
        group_prgs = []

print 'Total number of different program groups:    ', len(groups)