import pygame
import time
from config import Config
from rule_functions import *
from initialization import *

class CellularAutomaton:

    def __init__(self, N, r, rule_function, ic_function = get_random_ic, **kwargs):

        # ic_function_kwargs = {key: kwargs[key] for key in kwargs if key in ic_function.__code__.co_varnames}
        # rule_function_kwargs = {key: kwargs[key] for key in kwargs if key in rule_function.__code__.co_varnames}

        self.N = N
        self.r = r
        self.dna = rule_function(r, **kwargs) # rule_dict

    def simulate(self, height, ic, stop = float('inf'), show_time = True, delay = 0.1):

        self.history = [ic]

        cells_on_screen = [self.history[0][:]] + [[-1 for _ in range(self.N)] for _ in range(height - 1)]

        pygame.init()
        screen = pygame.display.set_mode((self.N*10, height*10))
        pygame.display.set_caption('Cellular Automaton')

        running = True
        pause = False

        t = 0
        
        while t <= stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = not pause
            
            if not pause:
                t += 1
                draw_cells(screen, cells_on_screen)

                new_cells = get_new_cells(self.dna, self.history[-1][:], self.r)
                self.history.append(new_cells[:])

                if t < height:
                    cells_on_screen.insert(t, new_cells)
                    cells_on_screen.pop()
                else:
                    cells_on_screen.pop(0)
                    cells_on_screen.append(new_cells)

                if show_time:
                    render_text_with_border(screen, t, self.N)
                pygame.display.flip()
                time.sleep(delay)

        pygame.quit()

    def run(self, ic, stop= None):

        self.history = [ic]

        if stop == None:
            stop = 2*self.N

        t = 0
        
        while t <= stop:
            new_cells = get_new_cells(self.dna, self.history[-1][:], self.r)
            self.history.append(new_cells[:])

            t += 1

        return self.history[-1]


if __name__ == '__main__':

    N = Config.N
    delay = Config.delay
    height = Config.height
    r = Config.radius
    rule = Config.rule

    N = 50
    r = 1
    rule = 110

    automaton1 = CellularAutomaton(N, r, get_all_black)
    automaton2 = CellularAutomaton(N, r, get_wolfram_rule, rule = rule)

    ic = get_uniformly_distributed_ic(N, predominant_color=1)

    automaton2.simulate(height, ic)
