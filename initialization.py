import random
from config import Config

def get_random_ic(N): 
    
    return [random.choice([0, 1]) for _ in range(N)]

def get_custom_ic(N):
    
    ic = Config.custom_ic
    
    return ic

def get_uniformly_distributed_ic(N, predominant_color=None):
    """
    Generate an initial configuration with a density ρ uniformly distributed over [0.0, 1.0]
    ρ ∈ [0.0, 1.0]

    Parameters:
    - N (int): The size of the configuration.
    - predominant_color (str): If 'black', ensures more black cells; if 'white', ensures more white cells.

    Returns:
    list: A list representing the initial configuration with a uniformly distributed density.
    """

    density = random.uniform(0.0, 1.0)

    a = int(N * density)
    b = N - a

    if predominant_color == 1:
        ones_count = max(a, b)
        zeros_count = min(a, b)
    elif predominant_color == 0:
        zeros_count = max(a, b)
        ones_count = min(a, b)
    else:
        zeros_count = a
        ones_count = b

    initial_config = [1] * ones_count + [0] * zeros_count
    random.shuffle(initial_config)
    return initial_config

if __name__ == '__main__':
    
    N = 5
    initial_config_default = get_uniformly_distributed_ic(N)[0]
    initial_config_black = get_uniformly_distributed_ic(N, predominant_color=1)[0]
    initial_config_white = get_uniformly_distributed_ic(N, predominant_color=0)[0]