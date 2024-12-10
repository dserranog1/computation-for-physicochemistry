import random
import numpy as np
import pygame
import matplotlib.pyplot as plt
from datetime import datetime
import os

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


class BaseAutomaton:
    """Base class for automata. Subclasses must implement their own get_direction method."""

    def __init__(self, position):
        self.position = position
        self.color = (0, 0, 0)

    def get_direction(self):
        """
        Get the direction in which this automaton should move.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement get_direction.")


class AutomatonA(BaseAutomaton):
    def __init__(self, position):
        super().__init__(position)
        self.automaton_type = "A"
        self.color = (50, 50, 255)

    # Bias towards down by including DOWN multiple times
    directions = [DOWN, DOWN, DOWN, UP, LEFT, RIGHT]

    def get_direction(self):
        return random.choice(self.directions)


class AutomatonB(BaseAutomaton):
    def __init__(self, position):
        super().__init__(position)
        self.automaton_type = "B"
        self.color = (50, 225, 50)

    # Bias towards up by including UP multiple times
    directions = [UP, UP, DOWN, LEFT, RIGHT]

    def get_direction(self):
        return random.choice(self.directions)


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.occupancy = np.full((height, width), None, dtype=object)

    def is_occupied(self, position):
        y, x = position
        return self.occupancy[y, x] is not None

    def update_cell(self, automaton, old_position=None):
        if old_position:
            old_y, old_x = old_position
            self.occupancy[old_y, old_x] = None
        y, x = automaton.position
        self.occupancy[y, x] = automaton

    def get_random_empty_cell(self):
        """Return the coordinates of a random empty cell on the grid."""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not self.is_occupied((y, x)):
                return (y, x)


def draw_grid(
    surface: pygame.Surface,
    grid,
    cell_size,
):
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.occupancy[y, x]:
                automaton = grid.occupancy[y, x]
                color = automaton.color
                pygame.draw.rect(
                    surface, color, (x * cell_size, y * cell_size, cell_size, cell_size)
                )


class Simulation:
    def __init__(
        self,
        number_of_automaton = 50,
        steps = 1000,
        number_of_graphs = 1,
        screen_width=500,
        screen_height=500,
        grid_width=50,
        grid_height=50,
    ):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = self.screen_width // self.grid_width
        self.number_of_automaton = number_of_automaton
        self.steps = steps
        self.number_of_graphs = number_of_graphs

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Cellular Automaton Simulation")
        self.clock = pygame.time.Clock()

        self.grid = Grid(self.grid_height, self.grid_width)
        self.automata = []

        # Generate the simulation directory with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.output_dir = f"automatas/simulation_{timestamp}"
        os.makedirs(self.output_dir, exist_ok=True)

        self._initialize_automata()

    def _initialize_automata(self):
        automatas = [AutomatonA, AutomatonB]
        for automaton_class in automatas:
            for _ in range(self.number_of_automaton):
                random_initial_position = self.grid.get_random_empty_cell()
                new_automaton = automaton_class(random_initial_position)
                self.grid.update_cell(new_automaton)
                self.automata.append(new_automaton)

    def _move_automaton(self, automaton):
        y, x = automaton.position

        dy, dx = automaton.get_direction()

        new_y = y + dy
        new_x = x + dx

        # Vertical boundaries: no wrapping
        if new_y < 0 or new_y >= self.grid_height:
            new_y = y

        # Horizontal wrapping
        new_x = new_x % self.grid_width

        # Move if free
        if not self.grid.is_occupied((new_y, new_x)) or (new_y == y and new_x == x):
            automaton.position = (new_y, new_x)
            self.grid.update_cell(automaton=automaton, old_position=(y, x))

    def get_row_distribution(self):
        """
        Count how many automata are in each row at the current state and return as a list.
        """
        row_counts = [0] * self.grid_height
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if self.grid.occupancy[y, x] is not None:
                    row_counts[y] += 1
        return row_counts

    def save_histogram(self, row_counts, step):
        """
        Save a histogram of the current row distribution to a file in the simulation directory.
        """
        plt.figure(figsize=(6, 10))
        plt.barh(range(len(row_counts)), row_counts, color="blue")
        plt.ylabel("Row")
        plt.xlabel("Number of Automata")
        plt.title(f"Distribution of Automata at Step {step}")
        plt.savefig(os.path.join(self.output_dir, f"histogram_{step}.png"))
        plt.close()

    def run(self):
        """
        Run the main simulation loop until the user closes the window or we reach a set number of steps.
        """
        number_of_histograms = 6
        step = 0
        row_counts = self.get_row_distribution()
        self.save_histogram(row_counts, step)
        while step < self.steps:
            step += 1
            self.screen.fill((255, 255, 255))  # Clear screen
            draw_grid(self.screen, self.grid, self.cell_size)
            pygame.display.flip()

            # Attempt to move each automaton once per iteration
            for automaton in self.automata:
                self._move_automaton(automaton)

            if step % (self.steps / self.number_of_graphs) == 0:
                row_counts = self.get_row_distribution()
                self.save_histogram(row_counts, step)

            self.clock.tick(60)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    step = self.steps

        pygame.quit()


if __name__ == "__main__":
    number_of_automaton = 300
    steps = 300
    number_of_graphs = 6
    sim = Simulation(number_of_automaton, steps, number_of_graphs)
    sim.run()

    # After the simulation ends, produce a final histogram
    row_counts = sim.get_row_distribution()
    sim.save_histogram(row_counts, "final")