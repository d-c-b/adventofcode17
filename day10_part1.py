with open('input_d10.txt', 'rU') as f:
  input_lengths = f.readline().split(',')

input_lengths = map(int, input_lengths)

number_list = range(256)

skip_size = 0
position_indx = 0


for length in input_lengths:
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
    
print number_list
mult_first_two = number_list[0] * number_list[1]
print '        '
print '        '
print 'Multiplication of first two numbers in list = ', mult_first_two