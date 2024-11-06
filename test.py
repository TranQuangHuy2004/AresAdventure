from maze import Maze
from Search_algorithm.bfs import bfs
from Search_algorithm.dfs import dfs
from Search_algorithm.ucs import ucs
from Search_algorithm.a_star import a_star

import psutil
import os

# inner psutil function


def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / 1024 ** 2

# decorator function


def profile(func):
    def wrapper(*args, **kwargs):

        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))

        return result
    return wrapper

# instantiation of decorator function


filename = "input-06.txt"


@profile
# main code for which
# memory has to be monitored
def bfs_alg():
    maze = Maze()
    maze.read_from_file(filename)
    result = bfs(maze.Ares_position, maze.stones_positions,
                 maze.grid, maze.weights, maze.switch_positions)
    print(result)


@profile
def dfs_alg():
    maze = Maze()
    maze.read_from_file(filename)
    result = dfs(maze.Ares_position, maze.stones_positions,
                 maze.grid, maze.weights, maze.switch_positions)
    print(result)


@profile
def ucs_alg():
    maze = Maze()
    maze.read_from_file(filename)
    result = ucs(maze.Ares_position, maze.stones_positions,
                 maze.grid, maze.weights, maze.switch_positions)
    print(result)


@profile
def a_star_alg():
    maze = Maze()
    maze.read_from_file(filename)
    result = a_star(maze.Ares_position, maze.stones_positions,
                    maze.grid, maze.weights, maze.switch_positions)
    print(result)


bfs_alg()
dfs_alg()
ucs_alg()
a_star_alg()
