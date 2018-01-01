with open('input_d12.txt', 'rU') as f:
  pipe_connections = f.read().split('\n')


group_0_progs = [0]

def find_connected_progs(prg_num):
    connections = map(int, pipe_connections[prg_num].split(' <-> ')[-1].split(', '))

    for connection in connections:
        already_done = connection in group_0_progs
        if already_done == False:
            group_0_progs.append(connection)
            find_connected_progs(connection)

find_connected_progs(0)

group_0_count = len(group_0_progs)
print 'Number of programs in group containing program 0:   ', group_0_count