import random

def randomize(N, current_cells):

    new_cells = [random.choice([0, 1]) for _ in range(N)]

    return new_cells

def get_all_black(N, current_cells):

    new_cells = [1 for _ in range(N)]

    return new_cells

def get_all_white(N, current_cells):

    new_cells = [0 for _ in range(N)]

    return new_cells