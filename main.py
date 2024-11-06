from maze import Maze
from Search_algorithm.bfs import bfs
from Search_algorithm.dfs import dfs
from Search_algorithm.ucs import ucs
from Search_algorithm.a_star import a_star
from output_file import output

from GUI.home import home
from GUI.algorithm import alg
from GUI.visualization import visual

import time
import psutil

from tkinter import *
from ctypes import windll


def show_home():
    view1 = home(root, show_alg, show_visual)
    view1.display()


def show_alg():
    view2 = alg(root, show_home)
    view2.display()


def show_visual():
    view3 = visual(root, show_home)
    view3.display()


def main():
    windll.shcore.SetProcessDpiAwareness(1)
    global root
    root = Tk()

    show_home()

    root.mainloop()

    # output(maze, "Output-01.txt")

    # filename = "output-04.txt"
    # bfs_output_file(maze, filename)
    # dfs_output_file(maze, filename)
    # ucs_output_file(maze, filename)
    # a_star_output_file(maze, filename)

    # maze = Maze()
    # maze.read_from_file("input/input-02.txt")

    # result = bfs(maze.Ares_position, maze.stones_positions,
    #              maze.grid, maze.weights, maze.switch_positions)
    # print(result)
    # print("")
    # print(len(result[2]))

    # result = dfs(maze.Ares_position, maze.stones_positions,
    #              maze.grid, maze.weights, maze.switch_positions)
    # print(result)
    # print("")
    # print(len(result[2]))

    # result = ucs(maze.Ares_position, maze.stones_positions,
    #              maze.grid, maze.weights, maze.switch_positions)
    # print(result)
    # print("")
    # print(len(result[2]))

    # result = a_star(maze.Ares_position, maze.stones_positions,
    #                 maze.grid, maze.weights, maze.switch_positions)
    # print(result)
    # print("")
    # print(len(result[2]))


if __name__ == "__main__":
    main()
