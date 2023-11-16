import matplotlib.pyplot as plt
import numpy as np

class CellularAutomaton:
    def __init__(self, N):
        self.N = N  # lattice_size
        self.cells = np.zeros(N)
        self.evolve_history = []  # List to store the evolution history

    def visualize_cells(self):
        plt.imshow(self.evolve_history, cmap='gray_r', aspect='auto', extent=(0, self.N, 0, len(self.evolve_history)))
        plt.pause(1)

    def randomize_cells(self, density=0.5):
        self.cells = np.random.choice([0, 1], size=self.N, p=[1 - density, density])

    def evolve_and_visualize(self, generations):
        for _ in range(generations):
            self.evolve()
            self.evolve_history.append(np.copy(self.cells))  # Store the current state for visualization
            self.visualize_cells()

    def evolve(self, density=0.5):
        self.cells = np.random.choice([0, 1], size=self.N, p=[1 - density, density])

# Example usage:
automaton = CellularAutomaton(N=100)
automaton.randomize_cells(density=0.3)
automaton.evolve_and_visualize(generations=100)
