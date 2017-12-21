with open('input_d9.txt', 'rU') as f:
  input_string = f.read()

group_stack = []
nest_count = 0
score_count = 0


def prev_is_exclamation(char):
  if char == '!':
    return True
  else:
    return False


def stack_last_entry_condition():
    if (len(group_stack) > 0):
      if (group_stack[-1] != '<' ):
        return 0
      else:
        return 1
    else:
      return 2

def remove_unnecessary_exclamations(input_str):
    return input_str.replace("!!","")


def find_score_of_string(input_str):
    score_count = 0
    nest_count = 0
    for i in range(len(input_str)):
         if (prev_is_exclamation(input_str[i-1]) == False):
             if (stack_last_entry_condition() == 0):
                 if (input_str[i] == '{'):
                     group_stack.append(input_str[i])
                     nest_count += 1

                 elif (input_str[i] == '}') and (group_stack[-1] == '{'):
                    score_count += nest_count
                    del group_stack[-1]
                    nest_count -= 1


                 elif (input_str[i] == '>') and (group_stack[-1] == '<'):
                    del group_stack[-1]

                 elif (input_str[i] == '<'):
                    group_stack.append(input_str[i])

             elif (stack_last_entry_condition() == 1):
                    if (input_str[i] == '>'):
                        del group_stack[-1]

             elif (stack_last_entry_condition() == 2):
                 if (input_str[i] == '{'):
                     group_stack.append(input_str[i])
                     nest_count += 1
                     i += 1

                 elif (input_string[i] == '<'):
                     group_stack.append(input_string[i])

    return score_count


inpt = remove_unnecessary_exclamations(input_string)
score = find_score_of_string(inpt)

print 'Total Score: ', score
