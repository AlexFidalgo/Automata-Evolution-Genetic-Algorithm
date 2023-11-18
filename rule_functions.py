import random

def randomize(N):

    new_cells = [random.choice([0, 1]) for _ in range(N)]

    return new_cells

def get_all_black(N):

    new_cells = [1 for _ in range(N)]

    return new_cells

def get_all_white(N):

    new_cells = [0 for _ in range(N)]

    return new_cells