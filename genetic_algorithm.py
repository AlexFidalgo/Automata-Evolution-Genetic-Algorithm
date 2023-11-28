import random
import time
import sys
from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *
from fitness_evaluation import *

class Population:

    def __init__(self, N, r, pop_size, mutation_rate = 0.02):

        self.pop_size = pop_size
        self.population = [Chromosome(N, r, get_rule_from_flat_distribution) for _ in range(pop_size)]
        self.F = [] # fitness list
        self.generations = 0
        self.mutation_rate = mutation_rate
        self.N = N

    def evolve(self, elite_members_fraction = 0.2, use_pred_color = True, number_of_ics = 100):

        self.set_fitness(number_of_ics = number_of_ics, use_pred_color = use_pred_color)
        self.order_population()

        elite_members = int(elite_members_fraction*self.pop_size)

        next_generation = self.population[:elite_members]

        for _ in range(self.pop_size - elite_members):

            c1 = random.choice(next_generation)
            c2 = random.choice(next_generation)

            c = c1.crossover(c2)

            c.mutate(self.mutation_rate)

            next_generation.append(c)

        self.population = next_generation
        self.generations += 1
            
    def order_population(self):

        sorted_pairs = sorted(zip(self.population, self.F), key=lambda x: x[1], reverse=True)
        self.population = [pair[0] for pair in sorted_pairs]

    def set_fitness(self, number_of_ics = 100, use_pred_color = True):

        ic_list = []
        ic_color = []

        for i in range(number_of_ics):
                if use_pred_color:
                    color = i%2
                    ic_list.append(get_uniformly_distributed_ic(self.N, predominant_color=color))   
                else:
                    ic = get_uniformly_distributed_ic(self.N)
                    color = get_pred_color(ic)
                    ic_list.append(ic)
                ic_color.append(color)

        self.F = []

        for c in self.population:
            self.F.append(c.run_multiple(ic_list, ic_color))


    def get_max_fitness(self):

        if self.F:
            return max(self.F)
        return None

class Chromosome(CellularAutomaton):

    def __init__(self, N, r, rule_function, ic_function=get_uniformly_distributed_ic, **kwargs):
        super().__init__(N, r, rule_function, ic_function, **kwargs)

    def show_dna(self):
        print(self.dna)

    def mutate(self, mutation_rate=0.02):

        points_to_mutate = int(mutation_rate*self.N)

        for i in range(points_to_mutate):

            random_key = random.choice(list(self.dna.keys()))
            if self.dna[random_key] == 0:
                self.dna[random_key] = 1
            elif self.dna[random_key] == 1:
                self.dna[random_key] = 0

    def crossover(self, other):

        dna_values1 = list(self.dna.values())
        dna_values2 = list(other.dna.values())

        if self.N == other.N:

            crossover_point = random.randint(0, self.N)

        else:
            raise Exception("Chromosomes have different lenghts")

        dna_values = dna_values1[:crossover_point] + dna_values2[crossover_point:]

        dna = dict(zip(self.dna.keys(), dna_values))

        return Chromosome(self.N, self.r, dna)

    def run_multiple(self, ic_list, ic_color, stop = None):

        got_right = 0

        for ic, color in zip(ic_list, ic_color):
            
            last_res, penultimate_res = self.run(ic)

            if is_result_correct(last_res, color) and is_result_correct(penultimate_res, color):
                got_right += 1

        fitness = calculate_fitness(got_right, len(ic_list))

        return fitness



if __name__ == '__main__':

    r = 3
    N = 149
    pop_size = 100
    mutation_rate = 0.02
    generations = 100
    use_pred_color = False
    manual = False

    start_time = time.time()
    p = Population(N, r, pop_size, mutation_rate)

    p.set_fitness(use_pred_color=use_pred_color)
    print(f"Initial maximum fitness: {p.get_max_fitness()}")

    if manual:
        ret = user_option(p, use_pred_color=use_pred_color)
        if ret == 'q':
            sys.exit(0)

    for i in range(generations):

        elapsed_time_seconds = time.time() - start_time
        hours = int(elapsed_time_seconds // 3600)
        minutes = int((elapsed_time_seconds % 3600) // 60)
        print(f"{int(hours)}h{int(minutes)}min")


        p.evolve(use_pred_color=use_pred_color)

        print(f"Current generation: {p.generations}")
        print(f"Current fitness: --------> {p.get_max_fitness()}")



