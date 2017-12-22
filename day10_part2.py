with open('input_d10.txt', 'rU') as f:
  input_lengths = f.readline()

input_ascii = map(ord, input_lengths)

input_ascii += [17, 31, 73, 47, 23]

number_list = range(256)

def iteration_knot_hash(skip_size, position_indx):
    
    for length in input_ascii:
        if length != 0:
            end_indx = (position_indx+length) % len(number_list)

            if end_indx > position_indx:
                sub_list = number_list[position_indx:end_indx]
                rev_sub_list = sub_list[::-1]
                number_list[position_indx:end_indx] = rev_sub_list
                pos_indx = position_indx + (length + skip_size)
                position_indx = pos_indx % len(number_list)
                skip_size += 1
  
            elif end_indx <= position_indx:
                sub_list = number_list[position_indx:] + number_list[:end_indx]
                rev_sub_list = sub_list[::-1]
                number_list[position_indx:] = rev_sub_list[:(len(number_list)-position_indx)]
                number_list[:(len(rev_sub_list)-len(number_list)+position_indx)] = rev_sub_list[(len(number_list)-position_indx):]
                pos_indx = position_indx + (length + skip_size)
                position_indx = pos_indx % len(number_list)
                skip_size += 1

        elif length == 0:
            skip_size += 1    

    return skip_size, position_indx

skp_sze = 0
posit_index = 0

for i in range(64):
    skp_sze, posit_index = iteration_knot_hash(skp_sze, posit_index)
    
    
dense_hash = []

split_number_list = [number_list[i:i + 16] for i in xrange(0, 256, 16)]

for split_list in split_number_list:
    condensed = reduce(lambda i, j : i ^ j, split_list )
    dense_hash.append(condensed)

hexadecimal_string = ''


for num in dense_hash:
    hx_val = format(num, 'x')
    hexadecimal_string += hx_val
    
print 'Hexadecimal string of knot hash:   ', hexadecimal_string
