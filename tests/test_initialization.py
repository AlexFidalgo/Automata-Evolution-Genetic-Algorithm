import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from initialization import *

def test_get_uniformly_distributed_ic(num_iterations, N=51, predominant_color=None):
    densities = []

    for _ in range(num_iterations):
        initial_config = get_uniformly_distributed_ic(N, predominant_color)[0]
        density_of_ones = sum(initial_config) / N
        densities.append(density_of_ones)

    # Plotting the distribution
    plt.hist(densities, bins=20, edgecolor='black')
    plt.title('Distribution of Densities in Initial Configurations')
    plt.xlabel('Density of Ones')
    plt.ylabel('Frequency')
    plt.show()

num_iterations = 1000
test_get_uniformly_distributed_ic(num_iterations)