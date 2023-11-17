import pygame
import random
import time

class CellularAutomaton:

    def __init__(self, N):

        self.N = N
        self.width = self.N
        self.height = 10
        self.cells = [[random.choice([0, 1]) for _ in range(self.N)]] + [[-1 for _ in range(self.N)] for _ in range(self.height - 1)]

    def draw_cells(self, screen):

        # self.cells = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.height)]
        self.history = [None] * self.height

        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell == -1:
                    color = (220, 220, 220)
                else:
                    color = (0, 0, 0) if cell == 0 else (255, 255, 255)
                pygame.draw.rect(screen, color, (j * 10, i * 10, 10, 10))

    def randomize(self):
        new_cells = [random.choice([0, 1]) for _ in range(self.N)]

        if self.t < self.height:
            self.cells.insert(self.t, new_cells)
            self.cells.pop()
        else:
            self.cells.pop(0)
            self.cells.append(new_cells)

    def simulate(self, generations):

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

            time.sleep(1)

        pygame.quit()

if __name__ == '__main__':
    automaton = CellularAutomaton(N=10)
    automaton.simulate(generations=100)
