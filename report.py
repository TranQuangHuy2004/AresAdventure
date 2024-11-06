from maze import Maze
from Search_algorithm.bfs import bfs
from Search_algorithm.dfs import dfs
from Search_algorithm.ucs import ucs
from Search_algorithm.a_star import a_star
from output_file import output

from GUI.home import home
from GUI.algorithm import alg
from GUI.visualization import visual

maze = Maze()
maze.read_from_file("input/input-11.txt")

# print(maze.max_width_max_height())
# print(maze.Ares_position)
# print(maze.stones_positions)
# print(maze.weights)
# print(maze.switch_positions)
result = bfs(maze.Ares_position, maze.stones_positions,
             maze.grid, maze.weights, maze.switch_positions)
print(result)
print("")

result = dfs(maze.Ares_position, maze.stones_positions,
             maze.grid, maze.weights, maze.switch_positions)
print(result)
print("")

result = ucs(maze.Ares_position, maze.stones_positions,
             maze.grid, maze.weights, maze.switch_positions)
print(result)
print("")
result = a_star(maze.Ares_position, maze.stones_positions,
                maze.grid, maze.weights, maze.switch_positions)
print(result)
print("")
