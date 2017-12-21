with open('input_d9.txt', 'rU') as f:
  input_string = f.read()

def prev_is_exclamation(char):
  if char == '!':
    return True
  else:
    return False

def remove_unnecessary_exclamations(input_str):
    return input_str.replace("!!","")


def count_uncancelled_garbage(input_str):
    group_stack = []
    garbage_count = 0
    i = 0
    while i < len(input_str):
        if prev_is_exclamation(input_str[i-1]) == False:
            if (len(group_stack) == 0) and (input_str[i] != '<'):
                i += 1
            elif (len(group_stack) == 0) and (input_str[i] == '<'):
                group_stack.append(input_str[i])
                i += 1
            elif (len(group_stack) == 1) and (input_str[i] == '>'):
                del group_stack[-1]
                i += 1
            elif (len(group_stack) == 1) and (input_str[i] == '!'):
                i += 1
            
            elif (len(group_stack) == 1) and (input_str[i] != '!'):
                garbage_count += 1
                i += 1
            
        elif prev_is_exclamation(input_str[i-1]) == True:
            i += 1
   
    return garbage_count     
        
inpt = remove_unnecessary_exclamations(input_string)
garb_count = count_uncancelled_garbage(inpt)

print 'Uncancelled Garbage Count = ', garb_count