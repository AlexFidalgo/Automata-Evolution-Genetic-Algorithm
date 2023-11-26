from genetic_algorithm import Chromosome
from rule_functions import *
from initialization import *

r = 1
N = 11
number_of_ics = 100

c1 = Chromosome(N, r, get_all_black)
c2 = Chromosome(N, r, get_all_white)

ic_list = []
ic_color = []

for i in range(number_of_ics):
        color = i%2
        ic_list.append(get_uniformly_distributed_ic(N, predominant_color=color))
        ic_color.append(color)

for i in range(10):

    c = Chromosome(N, r, get_rule_from_flat_distribution)
    print(f"c fitness: {c.run_multiple(ic_list, ic_color)}")

