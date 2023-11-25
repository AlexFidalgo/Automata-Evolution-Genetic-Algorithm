from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *

class Population:

    def __init__():

        self.chromosomes



class Chromosome(CellularAutomaton):

    def __init__(self, N, r, rule_function, ic_function=get_random_ic, **kwargs):
        super().__init__(N, r, rule_function, ic_function, **kwargs)

    def show_dna(self):
        print(self.dna)





if __name__ == '__main__':

    N = 50
    r = 1
    
    c = Chromosome(N, r, get_rule_from_flat_distribution, get_uniformly_distributed_ic, predominant_color='black')

    result = c.run()

    print(result)

    delay = Config.delay
    height = Config.height

    # c.simulate(height = height, delay = delay)