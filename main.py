import pygame
import sys
from queue import PriorityQueue
from solver import Solver

# Constants
GRID_SIZE_X = 20  # Grid size (number of cells)
GRID_SIZE_Y = 23
CELL_SIZE = 30  # Size of each cell in pixels
WINDOW_SIZE = max(GRID_SIZE_X, GRID_SIZE_Y) * CELL_SIZE  # Size of the window

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Simple Path Planner")


#obstacles_map = [[
solver = Solver(GRID_SIZE_X, GRID_SIZE_Y)
#solver.set_obstacles(obstacles_map)

start = (0, 0)
goal = (GRID_SIZE_X - 1, GRID_SIZE_Y - 1)

path = solver.solve(start, goal)
map = solver.get_map(path)

def draw_grid():

    for x in range(GRID_SIZE_X):
        for y in range(GRID_SIZE_Y):
            if map[x][y] == 0:
                color = BLACK
            elif map[x][y] == 1:
                color = RED
            elif map[x][y] == 2:
                color = GREEN
            pygame.draw.rect(window, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(window, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)  # Grid lines

if __name__ == "__main__":
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(WHITE)
        draw_grid()
        pygame.display.flip()

    pygame.quit()
    sys.exit()
