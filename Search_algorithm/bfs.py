from collections import deque
import Search_algorithm.direction as dir
import time
import psutil


def bfs(initial_Ares_pos, initial_stones_pos, grid, stone_weights, switch_pos):
    process = psutil.Process()  # Get the current process
    start_memory = process.memory_info().rss / 1024 ** 2  # Start memory in MB
    start_time = time.perf_counter()  # Start time

    # If the initial state is the goal state -> return
    if all((stone_x, stone_y) in switch_pos for (stone_x, stone_y) in initial_stones_pos):
        end_time = time.perf_counter()  # End time
        end_memory = process.memory_info().rss / 1024 ** 2  # End memory in MB
        execution_time = end_time - start_time
        memory_usage = end_memory - start_memory
        return (0, 0, "", execution_time, memory_usage)

    generated_nodes = 0  # The number of nodes generated by the algorithm

    # FIFO queue with (Ares_position, Stones_positions, solution_path, pushed_weight)
    q = deque()
    q.append((initial_Ares_pos, initial_stones_pos, "", 0))

    visited = set()
    # initial_stones_positions is a list, and since lists are mutable, they are unhashable
    visited.add((initial_Ares_pos, tuple(initial_stones_pos)))

    while q:
        Ares_pos, stones_pos, solution_path, cost = q.popleft()

        # Explore all 4 directions
        for dir_index, (dx, dy) in enumerate(dir.DIRECTIONS):
            new_Ares_pos = (Ares_pos[0] + dx, Ares_pos[1] + dy)

            # Check walls - Assume that there are no holes on the walls
            if grid[new_Ares_pos[0]][new_Ares_pos[1]] == '#':
                continue  # Skip if Ares moves into a wall or out of bounds

            # Check if Ares is pushing a stone
            if new_Ares_pos in stones_pos:
                # Calculate stone position with the direction that Ares will push it
                stone_index = stones_pos.index(new_Ares_pos)
                new_stone_pos = (
                    stones_pos[stone_index][0] + dx, stones_pos[stone_index][1] + dy)
                # Check walls
                if new_stone_pos in stones_pos or grid[new_stone_pos[0]][new_stone_pos[1]] == "#":
                    continue

                generated_nodes += 1

                # Update the stone new position
                new_stones_pos = list(stones_pos)
                new_stones_pos[stone_index] = new_stone_pos

                # Append push action to solution path
                new_solution_path = solution_path + dir.PUSHES[dir_index]

                # Update cost
                new_cost = 1 + cost + stone_weights[stone_index]

                # Check goal state
                if all((stone_x, stone_y) in switch_pos for (stone_x, stone_y) in new_stones_pos):
                    end_time = time.perf_counter()  # End time
                    end_memory = process.memory_info().rss / 1024 ** 2  # End memory in MB
                    execution_time = end_time - start_time
                    memory_usage = end_memory - start_memory
                    return (new_cost, generated_nodes, new_solution_path, execution_time, memory_usage)

                # Add new state to the queue if not visited
                if (new_Ares_pos, tuple(new_stones_pos)) not in visited:
                    visited.add((new_Ares_pos, tuple(new_stones_pos)))
                    q.append((new_Ares_pos, new_stones_pos,
                             new_solution_path, new_cost))

            else:  # Ares just moves without pushing a stone
                generated_nodes += 1
                # Update cost
                new_cost = cost + 1
                # Append push action to solution path
                new_solution_path = solution_path + dir.MOVES[dir_index]

                # Add new state to the queue if not visited
                if (new_Ares_pos, tuple(stones_pos)) not in visited:
                    visited.add((new_Ares_pos, tuple(stones_pos)))
                    q.append((new_Ares_pos, stones_pos,
                             new_solution_path, new_cost))

    # No solution found
    end_time = time.perf_counter()  # End time
    end_memory = process.memory_info().rss / 1024 ** 2  # End memory in MB
    execution_time = end_time - start_time
    memory_usage = end_memory - start_memory
    return (0, generated_nodes, "Not Found", execution_time, memory_usage)
