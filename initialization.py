import random

def get_initial_configuration(N, ic = 'random'):

    if ic == 'random':
        return [[random.choice([0, 1]) for _ in range(N)]]

    elif ic == 'uniformly distributed':
        #randomly choosing ICs that are uniformly distributed over ρ ∈ [0.0, 1.0], with exactly half with ρ < ρc and half with ρ > ρc
        return None

    else:
        return [ic]