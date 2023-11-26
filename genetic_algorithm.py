from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *
from fitness_evaluation import *

class Population:

    def __init__():

        self.chromosomes



class Chromosome(CellularAutomaton):

    def __init__(self, N, r, rule_function, ic_function=get_random_ic, **kwargs):
        super().__init__(N, r, rule_function, ic_function, **kwargs)

    def show_dna(self):
        print(self.dna)

    def run_multiple(self, ic_list, ic_color, stop = None):

        got_right = 0

        for ic, color in zip(ic_list, ic_color):
            
            result = self.run(ic)

            if is_result_correct(result, color):
                got_right += 1

        fitness = calculate_fitness(got_right, len(ic_list))

        return fitness



if __name__ == '__main__':

    N = 51
    r = 1
    rule = 110
    height = Config.height
    
    # automaton1 = Chromosome(N, r, get_all_black)
    automaton2 = Chromosome(N, r, get_wolfram_rule, rule = rule)

    ic = get_uniformly_distributed_ic(N, predominant_color=1)

    