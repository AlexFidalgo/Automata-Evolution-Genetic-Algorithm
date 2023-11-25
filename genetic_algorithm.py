from cellular_automata import CellularAutomaton
from initialization import *
from rule_functions import *

class Population:

    def __init__():

        self.chromosomes




class Chromosome(CellularAutomaton):

    def __init__(self, N, r, ic_function=get_random_ic, **kwargs):

        super().__init__(N, r, ic_function, **kwargs)
        self.dna = get_rule_from_flat_distribution(r)

        self.initialize_rule_dict()

    def set_rule_dict(self):

        rule_size = 2**get_total_number_of_cells(self.r)

        self.rule_dict = {format(i, '0' + str(2*self.r + 1) + 'b'): self.dna[i] 
            for i in range(rule_size)}

    def initialize_rule_dict(self):

        rule_size = 2**get_total_number_of_cells(self.r)

        self.rule_dict = {format(i, '0' + str(2*self.r + 1) + 'b'): self.dna[i] 
                                for i in range(rule_size)}


    def get_dna_rule(self):

        current_cells = self.history[-1][:]

    def show_rule(self):
        print(self.rule_dict)



if __name__ == '__main__':

    N = 50
    r = 1
    
    c = Chromosome(N, r)

    c.show_rule()



    # delay = Config.delay
    # height = Config.height

    # c.simulate(height = height, rule_function = get_all_black, delay = delay)