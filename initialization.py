import random

def get_initial_configuration(N, ic='random'):
    
    if ic == 'random':
        return [[random.choice([0, 1]) for _ in range(N)]]

    elif ic == 'uniformly distributed':
        # Randomly choosing IC uniformly distributed over ρ ∈ [0.0, 1.0]
        density = random.uniform(0.0, 1.0)
        ones_count = int(N * density)
        zeros_count = N - ones_count
        initial_config = [1] * ones_count + [0] * zeros_count
        random.shuffle(initial_config)
        density_real = ones_count/(zeros_count + ones_count)
        return [initial_config]

    else:
        return [ic]


if __name__ == '__main__':

    N = 50
    initial_config_random = get_initial_configuration(N, ic='random')
    initial_config_uniform = get_initial_configuration(N, ic='uniformly distributed')