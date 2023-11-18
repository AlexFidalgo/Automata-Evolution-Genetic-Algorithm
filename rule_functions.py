import random

def randomize(N):

    new_cells = [random.choice([0, 1]) for _ in range(N)]

    return new_cells