from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *
from fitness_evaluation import *

class Population:

    def __init__(self, N, r, pop_size):

        self.chromosomes = [Chromosome(N, r, get_rule_from_flat_distribution) for _ in range(pop_size)]

    def order_chromosomes(self):

        sorted_pairs = sorted(zip(self.chromosomes, self.F), key=lambda x: x[1], reverse=True)
        self.chromosomes_ordered = [pair[0] for pair in sorted_pairs]

    def get_fitness(self, number_of_ics = 100):

        ic_list = []
        ic_color = []

        for i in range(number_of_ics):
                color = i%2
                ic_list.append(get_uniformly_distributed_ic(N, predominant_color=color))
                ic_color.append(color)

        self.F = []

        for c in self.chromosomes:
            self.F.append(c.run_multiple(ic_list, ic_color))

        self.order_chromosomes()

    def get_max_fitness(self):
        return max(self.F)

        
            

class Chromosome(CellularAutomaton):

    def __init__(self, N, r, rule_function, ic_function=get_random_ic, **kwargs):
        super().__init__(N, r, rule_function, ic_function, **kwargs)

    def show_dna(self):
        print(self.dna)

    def run_multiple(self, ic_list, ic_color, stop = None):

        got_right = 0

        for ic, color in zip(ic_list, ic_color):
            
            last_res, penultimate_res = self.run(ic)

            if is_result_correct(last_res, color) and is_result_correct(penultimate_res, color):
                got_right += 1

        fitness = calculate_fitness(got_right, len(ic_list))

        return fitness



if __name__ == '__main__':

    r = 1
    N = 50
    pop_size = 10

    p = Population(N, r, pop_size)
    p.get_fitness()
    
    1+1

