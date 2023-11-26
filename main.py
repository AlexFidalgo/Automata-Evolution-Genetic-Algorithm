from genetic_algorithm import Chromosome
from rule_functions import *

r = 1
N = 11
number_of_ics = 100

c1 = Chromosome(N, r, get_all_black)
c2 = Chromosome(N, r, get_all_white)

ic_list = []
ic_color = []

for i in range(number_of_ics):
        color = i%2
        ic.append(get_uniformly_distributed_ic(N, predominant_color=color))
        ic_color.append(color)

print(f"c1 fitness: {c1.run_multiple(ic_list, ic_color)}")
print(f"c2 fitness: {c2.run_multiple(ic_list, ic_color)}")

# c3 = Chromosome(N, r, get_rule_from_flat_distribution)