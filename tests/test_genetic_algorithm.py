import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rule_functions import *
from initialization import *
from genetic_algorithm import Chromosome

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

print(f"c1 fitness: {c1.run_multiple(ic_list, ic_color)}")
print(f"c2 fitness: {c2.run_multiple(ic_list, ic_color)}")
