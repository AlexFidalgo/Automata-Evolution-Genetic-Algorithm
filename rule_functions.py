import random

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

def rule_110():
    pass