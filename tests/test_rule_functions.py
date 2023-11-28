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

# def plot_distribution_histogram(num_iterations):
#     r = 1
#     total_combinations = get_number_of_combination_of_bits(get_total_number_of_cells(r))
#     counts = {i: 0 for i in range(total_combinations + 1)}

#     for _ in range(num_iterations):
#         rule = get_rule_from_flat_distribution(r)
#         density_of_ones = sum(list(rule.values()))
#         counts[density_of_ones] += 1

#     total_iterations = sum(counts.values())

#     # Calculate proportions
#     proportions = [count / total_iterations for count in counts.values()]

#     # Plot the histogram
#     plt.bar(counts.keys(), proportions)
#     plt.xlabel('Density of Ones')
#     plt.ylabel('Proportion')
#     plt.title(f'Distribution of Rules for {total_iterations} iterations')
#     plt.show()

def plot_distribution_histogram(num_iterations, r):
    ones_density_list = []

    for _ in range(num_iterations):
        rule_dict = get_rule_from_flat_distribution(r)
        ones_density = list(rule_dict.values()).count(1) / len(rule_dict)
        ones_density_list.append(ones_density)

    # Plotting the histogram
    plt.hist(ones_density_list, bins='auto', alpha=0.7, color='b')
    plt.title('Distribution of Ones Density')
    plt.xlabel('Ones Density')
    plt.ylabel('Frequency')
    plt.show()

num_iterations = 10000
r = 3
test_get_rule_from_flat_distribution(num_iterations, r)
# plot_distribution_histogram(num_iterations, r)

