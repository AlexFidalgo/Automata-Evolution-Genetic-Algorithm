import random
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rule_functions import *

def test_get_rule_from_flat_distribution(num_iterations):
    r = 1
    counts = {i: 0 for i in range(9)}

    for _ in range(num_iterations):
        rule = get_rule_from_flat_distribution(r)
        density_of_ones = sum(rule)
        counts[density_of_ones] += 1

    total_iterations = sum(counts.values())

    print(f"Results after {total_iterations} iterations:")
    for density, count in counts.items():
        proportion = count / total_iterations
        print(f"{density}/8: {proportion:.4f}")

num_iterations = 10000
test_get_rule_from_flat_distribution(num_iterations)
