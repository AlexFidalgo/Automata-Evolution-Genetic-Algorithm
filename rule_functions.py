import random
from utils import *

def randomize(current_cells):

    N = len(current_cells)

    new_cells = [random.choice([0, 1]) for _ in range(N)]

    return new_cells

def get_all_black(current_cells):

    N = len(current_cells)

    new_cells = [1 for _ in range(N)]

    return new_cells

def get_all_white(current_cells):

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

    
    