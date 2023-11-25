import random
from utils import *

def randomize(current_cells, r):

    N = len(current_cells)

    new_cells = [random.choice([0, 1]) for _ in range(N)]

    return new_cells

def get_all_black(r): #last wolfram_rule

    rule = get_total_number_of_possible_rules(r)

    rule_dict = get_rule_table(r, rule-1)

    return rule_dict

def get_all_white(r): #first wolfram_rule

    rule_dict = get_rule_table(r, rule)

    return rule_dict

def get_wolfram_rule(r, rule = 110):
    
    rule_dict = get_rule_table(r, rule)
    
    return rule_dict

def get_rule_from_flat_distribution(r):
    
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

    rule_dict = {format(i, '0' + str(2*r + 1) + 'b'): selected_rule[i] 
                for i in range(rule_size)}

    return rule_dict

    
    