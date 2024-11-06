from tkinter import *
from collections import deque
from Search_algorithm.direction import DIRECTIONS


class Maze:
    def __init__(self):
        self.weights = []  # List to store stone weights
        self.grid = []  # 2D list representing the maze grid
        self.Ares_position = None  # (row, col) of Ares
        self.stones_positions = []  # List of (row, col) for stones
        self.switch_positions = []  # List of (row, col) for switches
        self.walls = []  # List of (row, col) for walls
        self.ares_id = None  # Canvas id for ares
        self.stones_id = []  # List of canvas id for stones
        self.weights_id = []  # List of canvas id for weights

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            # First line: list of stone weights
            self.weights = list(map(int, file.readline().strip().split()))

            # Remaining lines: grid structure
            self.grid = []
            row_index = 0

            for line in file:
                line = line.rstrip()  # Remove any trailing whitespace/newline
                row = []
                for col_index, char in enumerate(line):
                    row.append(char)

                    if char == '@':  # Ares' position
                        self.Ares_position = (row_index, col_index)
                    elif char == '+':  # Ares on a switch
                        self.Ares_position = (row_index, col_index)
                        self.switch_positions.append((row_index, col_index))
                    elif char == '$':  # Stone's position
                        self.stones_positions.append((row_index, col_index))
                    elif char == '*':  # Stone on a switch
                        self.stones_positions.append((row_index, col_index))
                        self.switch_positions.append((row_index, col_index))
                    elif char == '.':  # Switch position
                        self.switch_positions.append((row_index, col_index))
                    elif char == '#':  # Wall position
                        self.walls.append((row_index, col_index))

                self.grid.append(row)
                row_index += 1

    def print_maze(self):
        for row in self.grid:
            print("".join(row))

    def display_maze(self, canvas, tile_size):
        # Clear the canvas before redrawing
        canvas.delete("all")
        self.stones_id.clear()
        self.weights_id.clear()

        # Draw blank cell inside maze
        inside = flood_fill(self.Ares_position, self.grid)
        for (a, b) in inside:
            x1, y1 = b * tile_size, a * tile_size
            x2, y2 = x1 + tile_size, y1 + tile_size
            canvas.create_rectangle(
                x1, y1, x2, y2, fill="lightgray", outline="black")

        rows = len(self.grid)
        for row in range(rows):
            cols = len(self.grid[row])
            for col in range(cols):
                x1, y1 = col * tile_size, row * tile_size
                x2, y2 = x1 + tile_size, y1 + tile_size

                # Draw walls
                if self.grid[row][col] == "#":
                    canvas.create_rectangle(
                        x1, y1, x2, y2, fill="maroon", outline="black")
                # Draw Ares
                if (row, col) == self.Ares_position:
                    self.ares_id = canvas.create_rectangle(x1 + 5, y1 + 5, x2 - 5,
                                                           y2 - 5, fill="green", outline="black")
                # Draw stones
                elif (row, col) in self.stones_positions:
                    stone_idx = self.stones_positions.index((row, col))
                    stone_id = canvas.create_oval(x1 + 3, y1 + 3, x2 - 3,
                                                  y2 - 3, fill="dimgray", outline="black")
                    self.stones_id.append(stone_id)
                    # Put weight on
                    center_x = (x1 + x2) / 2
                    center_y = (y1 + y2) / 2
                    weight_id = canvas.create_text(center_x, center_y, text=str(
                        self.weights[stone_idx]), fill="yellow", font="Aptos 10")
                    self.weights_id.append(weight_id)
                # Draw switches
                elif (row, col) in self.switch_positions:
                    canvas.create_oval(
                        x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="pink", outline="red")

    def max_width_max_height(self):
        max_h = len(self.grid)
        max_w = max(len(row) for row in self.grid)
        return (max_w, max_h)


def flood_fill(ares_pos, grid):
    q = deque()
    q.append(ares_pos)

    visited = set()
    visited.add(ares_pos)

    while q:
        a_pos = q.popleft()

        for (dx, dy) in DIRECTIONS:
            new_a_pos = (a_pos[0] + dx, a_pos[1] + dy)

            if grid[new_a_pos[0]][new_a_pos[1]] == '#':
                continue

            if (new_a_pos) not in visited:
                visited.add(new_a_pos)
                q.append(new_a_pos)

    return visited
