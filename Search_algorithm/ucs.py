import heapq
import Search_algorithm.direction as dir
import time
import psutil


def ucs(initial_Ares_pos, initial_stones_pos, grid, stone_weights, switch_pos):
    process = psutil.Process()  # Get the current process
    start_memory = process.memory_info().rss / 1024 ** 2  # Start memory in MB
    start_time = time.perf_counter()  # Start time

    generated_nodes = 0  # The number of nodes generated by the algorithm

    # Priority queue with (cost, pushed_weight, Ares_position, stones_positions, solution_path)
    pq = []
    heapq.heappush(pq, (0, initial_Ares_pos, initial_stones_pos, ""))

    best_cost = {}
    best_cost[(initial_Ares_pos, tuple(initial_stones_pos))] = 0

    while pq:
        current_cost, Ares_pos, stones_pos, solution_path = heapq.heappop(
            pq)

        # Check goal state
        if all((stone_x, stone_y) in switch_pos for (stone_x, stone_y) in stones_pos):
            end_time = time.perf_counter()  # End time
            end_memory = process.memory_info().rss / 1024 ** 2  # End memory in MB
            execution_time = end_time - start_time
            memory_usage = end_memory - start_memory
            return (current_cost, generated_nodes, solution_path, execution_time, memory_usage)

        # If the current cost is higher than the best known cost for this state, skip it
        if current_cost > best_cost[(Ares_pos, tuple(stones_pos))]:
            continue

        # Explore all 4 directions
        for dir_index, (dx, dy) in enumerate(dir.DIRECTIONS):
            new_Ares_pos = (Ares_pos[0] + dx, Ares_pos[1] + dy)

            # Check walls
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

                # Update generated_nodes
                generated_nodes += 1

                # Update cost
                new_cost = current_cost + 1 + stone_weights[stone_index]

                # Update the stone new position
                new_stones_pos = list(stones_pos)
                new_stones_pos[stone_index] = new_stone_pos

                # Append push action to solution path
                new_solution_path = solution_path + dir.PUSHES[dir_index]

                # If this is a new state or found with a lower cost, update
                if (new_Ares_pos, tuple(new_stones_pos)) not in best_cost or new_cost < best_cost[(new_Ares_pos, tuple(new_stones_pos))]:
                    best_cost[(new_Ares_pos, tuple(new_stones_pos))] = new_cost
                    heapq.heappush(pq, (new_cost, new_Ares_pos, new_stones_pos,
                                        new_solution_path))

            else:  # Ares just moves without pushing a stone
                # Update generated_nodes
                generated_nodes += 1

                # Update cost
                new_cost = current_cost + 1

                # Append push action to solution path
                new_solution_path = solution_path + dir.MOVES[dir_index]

                # Add new state to the queue if not visited
                if (new_Ares_pos, tuple(stones_pos)) not in best_cost or new_cost < best_cost[(new_Ares_pos, tuple(stones_pos))]:
                    best_cost[(new_Ares_pos, tuple(stones_pos))] = new_cost
                    heapq.heappush(pq, (new_cost, new_Ares_pos,
                                   stones_pos, new_solution_path))

    # No solution found
    end_time = time.perf_counter()  # End time
    end_memory = process.memory_info().rss / 1024 ** 2  # End memory in MB
    execution_time = end_time - start_time
    memory_usage = end_memory - start_memory
    return (0, generated_nodes, "Not Found", execution_time, memory_usage)