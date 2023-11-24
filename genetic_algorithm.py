from cellular_automata import CellularAutomaton
from config import Config
from rule_functions import *
from initialization import *

class Population:

    def __init__():

        self.chromosomes




class Chromosome(CellularAutomaton):

    def __init__(self, N, r, ic_function=get_random_ic, **kwargs):

        super().__init__(N, ic_function, **kwargs)
        self.dna = get_rule_from_flat_distribution(N, r)

    def show_rule(self):

        rule_size = 2**get_total_number_of_cells(r)

        rule_dict = {format(i, '0' + str(2*r + 1) + 'b'): self.dna[i] 
                    for i in range(rule_size)}

        print(rule_dict)



if __name__ == '__main__':

    N = 50
    r = 1
    
    c = Chromosome(N, r)

    c.show_rule()