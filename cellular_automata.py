import pygame
import time
from config import Config
from rule_functions import *
from initialization import *

class CellularAutomaton:

    def __init__(self, N, r, ic_function = get_random_ic, **kwargs):

        self.N = N
        self.width = self.N
        self.r = r
        self.history = ic_function(N, **kwargs)

    def simulate(self, height, rule_function, stop = float('inf'), show_time = True, delay = 0.1, **kwargs):

        cells_on_screen = [self.history[0][:]] + [[-1 for _ in range(self.N)] for _ in range(height - 1)]

        pygame.init()
        screen = pygame.display.set_mode((self.width*10, height*10))
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

                new_cells = rule_function(self.history[-1][:], self.r, **kwargs)
                self.history.append(new_cells[:])

                if t < height:
                    cells_on_screen.insert(t, new_cells)
                    cells_on_screen.pop()
                else:
                    cells_on_screen.pop(0)
                    cells_on_screen.append(new_cells)

                if show_time:
                    render_text_with_border(screen, t, self.width)
                pygame.display.flip()
                time.sleep(delay)

        pygame.quit()

    def run(self, rule_function, rule, r, stop= None):

        if stop == None:
            stop = 2*self.N

        t = 0
        
        while t <= stop:
            new_cells = rule_function(current_cells = self.history[-1][:], **kwargs)
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

    automaton = CellularAutomaton(N, r, ic_function = get_uniformly_distributed_ic, predominant_color = 'black')
    # automaton = CellularAutomaton(N, ic_function = get_random_ic)

    # automaton.simulate(height = height, rule_function = get_wolfram_rule, rule = rule, delay = delay)
    automaton.simulate(height = height, rule_function = get_all_black, delay = delay)

    final_cells = automaton.run(rule_function = get_wolfram_rule, rule = rule, r = r)

    print(automaton.history)