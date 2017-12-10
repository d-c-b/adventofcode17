with open('input_d8.txt', 'rU') as f:
  register_instructions = f.read().split('\n')

register_dictionary = {}

def condition_instruction(reg_instr):
    condition = reg_instr[5]
    if condition == '==':
        if register_dictionary[reg_instr[4]] == int(reg_instr[6]):
            return True
        else:
            return False
    elif condition == '!=':
        if register_dictionary[reg_instr[4]] != int(reg_instr[6]):
            return True
        else:
            return False
    elif condition == '<':
        if register_dictionary[reg_instr[4]] < int(reg_instr[6]):
            return True
        else:
            return False
    elif condition == '>':
        if register_dictionary[reg_instr[4]] > int(reg_instr[6]):
            return True
        else:
            return False
    elif condition == '>=':
        if register_dictionary[reg_instr[4]] >= int(reg_instr[6]):
            return True
        else:
            return False
    elif condition == '<=':
        if register_dictionary[reg_instr[4]] <= int(reg_instr[6]):
            return True
        else:
            return False

def implement_condition(reg_instr):
    if reg_instr[1] == 'inc':
        register_dictionary[reg_instr[0]] += int(reg_instr[2])
    elif reg_instr[1] == 'dec':
        register_dictionary[reg_instr[0]] -= int(reg_instr[2])
        

def carry_out_instructions():
    for register_instruction in register_instructions:
        if register_instruction.split()[0] not in register_dictionary:
            register_dictionary[register_instruction.split()[0]] = 0

        if register_instruction.split()[4] not in register_dictionary:
            register_dictionary[register_instruction.split()[4]] = 0
        r_inst = register_instruction.split()
        if condition_instruction(r_inst) == True:
            implement_condition(r_inst)
        else:
            continue
    
    dict_keys = register_dictionary.keys()
    dict_values = register_dictionary.values()
        
    print 'Largest Register: ', dict_keys[dict_values.index(max(dict_values))]
    print 'Largest Value: ', max(dict_values)
 
carry_out_instructions()