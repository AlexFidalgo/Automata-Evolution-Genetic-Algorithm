import random
from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *
from fitness_evaluation import *

class Population:

    def __init__(self, N, r, pop_size, mutation_rate = 0.01):

        self.pop_size = pop_size
        self.population = [Chromosome(N, r, get_rule_from_flat_distribution) for _ in range(pop_size)]
        self.F = [] # fitness list
        self.generations = 0

    def evolve(self, elite_members_fraction = 0.2):
        """
•	    In each generation, (1) a new set of 100 ICs was generated, (2) F100 was computed on this set for each rule in the population, (3) CAs in the population were ranked in order of fitness, 
        (4) the 20 highest fitness (“elite”) rules were copied to the next generation without modification, and (5) the remaining 80 rules for the next generation were formed by single-point 
        crossovers between randomly chosen pairs of elite rules. The parent rules were chosen from the elite with replacement—that is, an elite rule was permitted to be chosen any number of 
        times. The offspring from each crossover were each mutated at exactly two randomly chosen positions. This process was repeated for 100 generations for a single run of the GA
        """

        self.set_fitness
        self.order_population()

        elite_members = elite_members_fraction*self.pop_size

        next_generation = self.population[:elite_members]

        for _ in range(self.pop_size - elite_members):

            c1 = random.choice(next_generation)
            c2 = random.choice(next_generation)

            next_generation.append(c1.crossover(c2))

        self.population = next_generation
        self.generations += 1
            


    def order_population(self):

        sorted_pairs = sorted(zip(self.population, self.F), key=lambda x: x[1], reverse=True)
        self.chromosomes = [pair[0] for pair in sorted_pairs]

    def set_fitness(self, number_of_ics = 100):

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

    def mutate(self, mutation_rate=0.02):

        points_to_mutate = mutation_rate*self.N

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

    r = 1
    N = 50
    pop_size = 10

    p = Population(N, r, pop_size)
    p.set_fitness()
    
    1+1

