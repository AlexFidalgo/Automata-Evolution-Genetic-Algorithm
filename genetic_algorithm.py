from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *
from fitness_evaluation import *

class Population:

    def __init__(self, N, r, pop_size, mutation_rate = 0.01):

        self.population = [Chromosome(N, r, get_rule_from_flat_distribution) for _ in range(pop_size)]
        self.F = [] # fitness list
        self.generations = 0

    def order_population(self):

        sorted_pairs = sorted(zip(self.population, self.F), key=lambda x: x[1], reverse=True)
        self.chromosomes = [pair[0] for pair in sorted_pairs]

    def get_fitness(self, number_of_ics = 100):

        ic_list = []
        ic_color = []

        for i in range(number_of_ics):
                color = i%2
                ic_list.append(get_uniformly_distributed_ic(N, predominant_color=color))
                ic_color.append(color)

        self.F = []

        for c in self.population:
            self.F.append(c.run_multiple(ic_list, ic_color))


    def get_max_fitness(self):

        if self.F:
            return max(self.F)
        return None

        
            

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

