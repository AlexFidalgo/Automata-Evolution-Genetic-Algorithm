import pygame
import random
import time

class CellularAutomaton:

    def __init__(self, N):
        self.N = N
        self.height = 50
        self.cells = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.height)]
        self.history = [None] * self.height

    def draw_cells(self, screen):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if self.history[i] is None:
                    color = (220, 220, 220)
                else:
                    color = (0, 0, 0) if cell == 0 else (255, 255, 255)
                pygame.draw.rect(screen, color, (j * 10, i * 10, 10, 10))

    def randomize(self):
        new_cells = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.height)]
        self.cells = new_cells
        # self.history.pop()
        self.history.insert(0, new_cells)

    def simulate(self, generations):
        pygame.init()
        screen = pygame.display.set_mode((self.N*10, self.height*10))
        pygame.display.set_caption('Cellular Automaton')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_cells(screen)
            self.randomize()
            pygame.display.flip()

            time.sleep(1)

            if len(self.history) > generations:
                self.history.pop()

        pygame.quit()

if __name__ == '__main__':
    automaton = CellularAutomaton(N=10)
    automaton.simulate(generations=100)
