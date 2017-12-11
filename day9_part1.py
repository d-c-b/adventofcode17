with open('input_d9.txt', 'rU') as f:
  input_string = f.read()

group_stack = []
nest_count = 0
score_count = 0


def conditions_met(index):
    if input_string[index-1] != '!':
        return True
    elif (input_string[index-1] == '!') and (input_string[index-2] == '!'):
        return True
    else:
        return False


for i in range(len(input_string)):
    print i
    
    if conditions_met(i) == True:
        if (input_string[i] == '{') and (group_stack[-1] != '<'):
            group_stack.append(input_string[i])
            nest_count += 1
        
        elif (input_string[i] == '}') and (group_stack[-1] != '<'):
            score_count += nest_count
            del group_stack[-1]
            nest_count -= 1
        
        elif (input_string[i] == '<') and (group_stack[-1] != '<'):
            group_stack.append(input_string[i])
            
        elif (input_string[i] == '>'):
            del group_stack[-1]
    
    
    
print 'Total Score: ', score_count