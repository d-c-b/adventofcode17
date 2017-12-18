with open('input_d9.txt', 'rU') as f:
  input_string = f.read()

group_stack = []
nest_count = 0
score_count = 0


def exclamation_conditions_met(index):
    if input_string[index-1] != '!':
        return True
    else:
        return False

def prev_is_exclamation(char):
  if char == '!':
    return True
  else:
    return False


def stack_last_entry_condition(index):
    if (len(group_stack) > 0):
      if (group_stack[-1] != '<' ):
        return 0
      else:
        return 1
    else:
      return 2

def remove_unnecessary_exclamations():
  indices_double_exc = []
  print input_string.rfind('!!')







#for i in range(50):#len(input_string)):
    #print nest_count
i = 0
while i < len(input_string):
    print i
    if (prev_is_exclamation(input_string[i-1]) == False):

      exclam_count = 0
      if (stack_last_entry_condition(i) == 0):
        if (input_string[i] == '{'):
          group_stack.append(input_string[i])
          nest_count += 1
          i += 1

        elif (input_string[i] == '}') and (group_stack[-1] == '{'):
          score_count += nest_count
          del group_stack[-1]
          nest_count -= 1
          i += 1

        elif (input_string[i] == '>') and (group_stack[-1] == '<'):
          del group_stack[-1]
          i += 1

        elif (input_string[i] == '<'):
          group_stack.append(input_string[i])
          i += 1

      elif (stack_last_entry_condition(i) == 1):
        if (input_string[i] == '>'):
          del group_stack[-1]
          i += 1
        else:
          i += 1

      elif (stack_last_entry_condition(i) == 2):
        if (input_string[i] == '{'):
          group_stack.append(input_string[i])
          nest_count += 1
          i += 1

        elif (input_string[i] == '<'):
          group_stack.append(input_string[i])
          i += 1

    else:
      if input_string[i] == '!':
        exclam_count += 1
        i += 1
      elif input_string[i] != '!':
        if exclam_count is even:
          i += exclam_count
        elif exclam_count is odd:
          i += 1
      print input_string[i-1], input_string[i]
      continue



print 'Total Score: ', score_count
print group_stack
print len(input_string)

print input_string.rfind('!!')
print input_string[16737]
print input_string[16738]
print input_string[16739]
print input_string[16740]
