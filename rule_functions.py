import random
from utils import *

def randomize(current_cells):

    N = len(current_cells)

    new_cells = [random.choice([0, 1]) for _ in range(N)]

    return new_cells

def get_all_black(current_cells): #last wolfram_rule

    N = len(current_cells)

    new_cells = [1 for _ in range(N)]

    return new_cells

def get_all_white(current_cells): #first wolfram_rule

    N = len(current_cells)

    new_cells = [0 for _ in range(N)]

    return new_cells

def get_wolfram_rule(current_cells, rule = 110, r = 1):

    N = len(current_cells)
    
    rule_dict = get_rule_table(r, rule)
    
    new_cells = []
    
    for c in range(N):
        
        input_str = ''
        
        for i in range(-r, r+1):
            
            corrected_index = (c+i)%len(current_cells)
            
            input_str += str(current_cells[corrected_index])
            
        new_cells.append(rule_dict[input_str])
        
    return new_cells

def get_rule_from_flat_distribution(N, r):
    
    rule_size = 2**get_total_number_of_cells(r)

    list_of_candidate_rules = []

    # Iterate over all possible densities and assign a random rule for each
    for density in range(rule_size + 1):
        # Create a rule with the desired density
        ones_count = density
        zeros_count = rule_size - density
        rule = [1] * ones_count + [0] * zeros_count

        # Randomly shuffle the rule
        random.shuffle(rule)

        list_of_candidate_rules.append(rule)
        
    selected_rule = random.choice(list_of_candidate_rules)

    # rule_dict = {format(i, '0' + str(2*r + 1) + 'b'): selected_rule[i] 
    #             for i in range(rule_size)}

    return selected_rule

    
    