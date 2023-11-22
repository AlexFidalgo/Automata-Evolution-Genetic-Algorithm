class Config:
    
    # General parameters
    N = 100  # Size of the lattice
    radius = 0 # Radius considered
    rule = 0 # wolfram rule to be applied
    custom_ic = [1, 1, 1]

    # Simulation parameters
    height = 50 # number of vertical cells on screen
    delay = 0.1 # ms

    # Genetic Algorithm parameters
    population_size = 100

# last rule
#   radius = 0: 2**(2**1) - 1 = 3
#   radius = 1: 2**(2**3) - 1 = 255
#   radius = 2: 2**(2**5) - 1 = 4294967295
