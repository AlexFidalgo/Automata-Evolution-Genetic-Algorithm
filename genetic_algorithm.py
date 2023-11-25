from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *

class Population:

    def __init__():

        self.chromosomes



class Chromosome(CellularAutomaton):

    def __init__(self, N, r, rule_function, ic_function=get_random_ic, **kwargs):
        super().__init__(N, r, rule_function, ic_function, **kwargs)

        self.predominant_color = self.get_ic_predominant_color(**kwargs)

    def show_dna(self):
        print(self.dna)

    def get_ic_predominant_color(self, **kwargs):
        if 'predominant_color' in kwargs:
            return kwargs['predominant_color']

        sum_cells = sum(self.history[0])
        if sum_cells > self.N/2:
            return 1
        else:
            return 0

if __name__ == '__main__':

    N = 5
    r = 1
    
    c1 = Chromosome(N, r, get_rule_from_flat_distribution, get_uniformly_distributed_ic)
    c2 = Chromosome(N, r, get_rule_from_flat_distribution, get_uniformly_distributed_ic)

    result = c.run()

    print(result)

    # delay = Config.delay
    # height = Config.height
    # c.simulate(height = height, delay = delay)