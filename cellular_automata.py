import pygame
import random
import time
from config import Config

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
                    color = (0, 0, 0) if cell == 0 else (255, 255, 255)
                pygame.draw.rect(screen, color, (j * 10, i * 10, 10, 10))

    def randomize(self):
        new_cells = [random.choice([0, 1]) for _ in range(self.N)]
        self.history.append(new_cells[:])

        if self.t < self.height:
            self.cells_on_screen.insert(self.t, new_cells)
            self.cells_on_screen.pop()
        else:
            self.cells_on_screen.pop(0)
            self.cells_on_screen.append(new_cells)

    def simulate(self, height, delay):

        self.height = height
        self.cells_on_screen = [self.history[0][:]] + [[-1 for _ in range(self.N)] for _ in range(self.height - 1)]

        pygame.init()
        screen = pygame.display.set_mode((self.width*10, self.height*10))
        pygame.display.set_caption('Cellular Automaton')

        running = True
        self.t = 0
        while running:
            self.t += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_cells(screen)
            self.randomize()
            pygame.display.flip()

            time.sleep(delay)

        pygame.quit()


if __name__ == '__main__':

    N = Config.N
    generations = Config.generations
    delay = Config.delay
    height = Config.height

    automaton = CellularAutomaton(N)
    automaton.simulate(height, delay)
