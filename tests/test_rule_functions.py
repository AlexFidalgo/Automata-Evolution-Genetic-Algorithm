import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rule_functions import *

def test_get_rule_from_flat_distribution(num_iterations, r):
    total_combinations = get_number_of_combination_of_bits(get_total_number_of_cells(r))
    counts = {i: 0 for i in range(total_combinations + 1)}

    total_combinations = get_number_of_combination_of_bits(get_total_number_of_cells(r))

    for _ in range(num_iterations):
        rule = get_rule_from_flat_distribution(r)
        density_of_ones = sum(list(rule.values()))
        counts[density_of_ones] += 1

    total_iterations = sum(counts.values())

    print(f"Results after {total_iterations} iterations:")
    for density, count in counts.items():
        proportion = count / total_iterations
        print(f"{density}/{total_combinations}: {proportion:.4f}")

def plot_distribution_histogram(num_iterations, r):
    ones_density_list = []

    for _ in range(num_iterations):
        rule_dict = get_rule_from_flat_distribution(r)
        ones_density = list(rule_dict.values()).count(1) / len(rule_dict)
        ones_density_list.append(ones_density)
        
    bins= [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    plt.hist(ones_density_list, bins=100, color='blue', edgecolor='black')
    plt.title('Distribution of Ones Density')
    plt.xlabel('Ones Density')
    plt.ylabel('Frequency')
    plt.show()

num_iterations = 10000
r = 3
# test_get_rule_from_flat_distribution(num_iterations, r)
plot_distribution_histogram(num_iterations, r)

