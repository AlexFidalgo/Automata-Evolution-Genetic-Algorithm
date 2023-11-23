
def get_total_number_of_cells(r): 

    return 2*r + 1

def get_total_number_of_possible_rules(r):

    number_of_considered_cells = get_total_number_of_cells(r)

    return 2**(2**number_of_considered_cells)

def get_rule_table(r, rule):

    number_of_considered_cells = get_total_number_of_cells(r)
    total_number_of_bits = get_total_number_of_possible_rules(r)
    
    binary_string = bin(rule)[2:]
    bits_rule = format(int(binary_string, 2), f'0{total_number_of_bits}b')
    
    rule_dict = {}
    for i in range(total_number_of_bits):
        binary_representation = format(i, f'0{number_of_considered_cells}b')
        rule_dict[binary_representation] = int(bits_rule[total_number_of_bits -1 - i])
    
    return rule_dict


if __name__ == '__main__':

# last rule
#   radius = 0: 2**(2**1) - 1 = 3
#   radius = 1: 2**(2**3) - 1 = 255
#   radius = 2: 2**(2**5) - 1 = 4294967295

    print(get_total_number_of_cells(2))