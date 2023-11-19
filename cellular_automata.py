import pygame
import random
import time
from config import Config
from rule_functions import *

class CellularAutomaton:

    def __init__(self, N, ic = None):

        self.N = N
        self.width = self.N
        self.history =  self.get_initial_configuration(ic)

    def get_initial_configuration(self, ic):

        if ic == None:
            return [[random.choice([0, 1]) for _ in range(self.N)]]
        else:
            return [ic]

    def draw_cells(self, screen):

        for i, row in enumerate(self.cells_on_screen):
            for j, cell in enumerate(row):
                if cell == -1:
                    color = (220, 220, 220)
                else:
                    color = (255, 255, 255) if cell == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (j * 10, i * 10, 10, 10))

    def render_text_with_border(self, screen):

        border_color = (0, 0, 0)
        text = pygame.font.Font(None, 36).render(f"t = {self.t}", True, (255, 255, 0))
        border_text = pygame.font.Font(None, 36).render(f"t = {self.t}", True, border_color)
        text_position = (self.width * 10 - 80, 10)
        screen.blit(border_text, (text_position[0] - 1, text_position[1] - 1))
        screen.blit(border_text, (text_position[0] + 1, text_position[1] - 1))
        screen.blit(border_text, (text_position[0] - 1, text_position[1] + 1))
        screen.blit(border_text, (text_position[0] + 1, text_position[1] + 1))
        screen.blit(text, (self.width * 10 - 80, 10))

    def simulate(self, height, rule_function, delay = 0.1):

        self.height = height
        self.cells_on_screen = [self.history[0][:]] + [[-1 for _ in range(self.N)] for _ in range(self.height - 1)]

        pygame.init()
        screen = pygame.display.set_mode((self.width*10, self.height*10))
        pygame.display.set_caption('Cellular Automaton')

        running = True
        pause = False

        self.t = 0
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = not pause
            
            if not pause:
                self.t += 1
                self.draw_cells(screen)

                new_cells = rule_function(self.history[-1][:])
                self.history.append(new_cells[:])

                if self.t < self.height:
                    self.cells_on_screen.insert(self.t, new_cells)
                    self.cells_on_screen.pop()
                else:
                    self.cells_on_screen.pop(0)
                    self.cells_on_screen.append(new_cells)

                self.render_text_with_border(screen)
                pygame.display.flip()
                time.sleep(delay)

        pygame.quit()


if __name__ == '__main__':

    N = Config.N
    delay = Config.delay
    height = Config.height

    automaton = CellularAutomaton(N)
    automaton.simulate(height = height, rule_function = randomize, delay = delay)
