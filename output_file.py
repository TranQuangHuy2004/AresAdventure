from Search_algorithm.bfs import bfs
from Search_algorithm.dfs import dfs
from Search_algorithm.ucs import ucs
from Search_algorithm.a_star import a_star


def output(maze, outputname, solutionname):
    # BFS
    result_bfs = bfs(maze.Ares_position, maze.stones_positions,
                     maze.grid, maze.weights, maze.switch_positions)
    cost, node, solution_path, time, memory = result_bfs
    step = 0
    if (solution_path != "Not Found"):
        step = len(solution_path)
    time *= 1000
    output_bfs = "BFS\n" + "Steps: " + str(step) + ", Cost: " + str(cost) + ", Node: " + str(
        node) + ", Time (ms): " + str(time) + ", Memory (MB): " + str(memory) + "\n" + solution_path + "\n"

    # DFS
    result_dfs = dfs(maze.Ares_position, maze.stones_positions,
                     maze.grid, maze.weights, maze.switch_positions)
    cost, node, solution_path, time, memory = result_dfs
    step = 0
    if (solution_path != "Not Found"):
        step = len(solution_path)
    time *= 1000
    output_dfs = "DFS\n" + "Steps: " + str(step) + ", Cost: " + str(cost) + ", Node: " + str(
        node) + ", Time (ms): " + str(time) + ", Memory (MB): " + str(memory) + "\n" + solution_path + "\n"

    # UCS
    result_ucs = ucs(maze.Ares_position, maze.stones_positions,
                     maze.grid, maze.weights, maze.switch_positions)
    cost, node, solution_path, time, memory = result_ucs
    step = 0
    if (solution_path != "Not Found"):
        step = len(solution_path)
    time *= 1000
    output_ucs = "UCS\n" + "Steps: " + str(step) + ", Cost: " + str(cost) + ", Node: " + str(
        node) + ", Time (ms): " + str(time) + ", Memory (MB): " + str(memory) + "\n" + solution_path + "\n"

    # A*
    result_a_star = a_star(maze.Ares_position, maze.stones_positions,
                           maze.grid, maze.weights, maze.switch_positions)
    cost, node, solution_path, time, memory = result_a_star
    step = 0
    if (solution_path != "Not Found"):
        step = len(solution_path)
    time *= 1000
    output_a_star = "A*\n" + "Steps: " + str(step) + ", Cost: " + str(cost) + ", Node: " + str(
        node) + ", Time (ms): " + str(time) + ", Memory (MB): " + str(memory) + "\n" + solution_path + "\n"

    f = open(outputname, "w")
    f.write(output_bfs)
    f.write(output_dfs)
    f.write(output_ucs)
    f.write(output_a_star)
    f.close()

    solutionname
    f = open(solutionname, "w")
    output = result_bfs[2] + "\n" + result_dfs[2] + \
        "\n" + result_ucs[2] + "\n" + result_a_star[2]
    f.write(output)
    f.close()
