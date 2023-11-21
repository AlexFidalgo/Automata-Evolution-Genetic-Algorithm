import pygame
import time
from config import Config
from rule_functions import *
from initialization import *

class CellularAutomaton:

    def __init__(self, N, ic = None, distribution = 'random'):

        self.N = N
        self.width = self.N
        self.history = get_initial_configuration(N)

    def draw_cells(self, screen, cells_on_screen):

        for i, row in enumerate(cells_on_screen):
            for j, cell in enumerate(row):
                if cell == -1:
                    color = (220, 220, 220)
                else:
                    color = (255, 255, 255) if cell == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (j * 10, i * 10, 10, 10))

    def render_text_with_border(self, screen, t):

        border_color = (0, 0, 0)
        text = pygame.font.Font(None, 36).render(f"t = {t}", True, (255, 255, 0))
        border_text = pygame.font.Font(None, 36).render(f"t = {t}", True, border_color)
        text_position = (self.width * 10 - 80, 10)
        screen.blit(border_text, (text_position[0] - 1, text_position[1] - 1))
        screen.blit(border_text, (text_position[0] + 1, text_position[1] - 1))
        screen.blit(border_text, (text_position[0] - 1, text_position[1] + 1))
        screen.blit(border_text, (text_position[0] + 1, text_position[1] + 1))
        screen.blit(text, (self.width * 10 - 80, 10))

    def simulate(self, height, rule_function, rule, r, delay = 0.1, stop = float('inf'), show_time = True):

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
                self.draw_cells(screen, cells_on_screen)

                new_cells = rule_function(current_cells = self.history[-1][:], rule = rule, r = r)
                self.history.append(new_cells[:])

                if t < height:
                    cells_on_screen.insert(t, new_cells)
                    cells_on_screen.pop()
                else:
                    cells_on_screen.pop(0)
                    cells_on_screen.append(new_cells)

                if show_time:
                    self.render_text_with_border(screen, t)
                pygame.display.flip()
                time.sleep(delay)

        pygame.quit()

    def run(self, rule_function, rule, r, stop= None):

        if stop == None:
            stop = 2*self.N

        t = 0
        
        while t <= stop:
            new_cells = rule_function(current_cells = self.history[-1][:], rule = rule, r = r)
            self.history.append(new_cells[:])

            t += 1

        return self.history[-1]


if __name__ == '__main__':

    N = Config.N
    delay = Config.delay
    height = Config.height
    r = Config.radius
    rule = Config.rule

    r = 1
    rule = 110

    automaton = CellularAutomaton(N, ic = 'uniformly distributed')
    automaton.simulate(height = height, rule_function = get_wolfram_rule, rule = rule, r = r, delay = delay)
    # final_cells = automaton.run(rule_function = get_wolfram_rule, rule = rule, r = r)
