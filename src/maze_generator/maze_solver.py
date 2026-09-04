# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    maze_solver.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jazurek <jazurek@student.42.pl>           +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/28 21:23:11 by jazurek          #+#    #+#              #
#    Updated: 2026/09/02 21:12:23 by jazurek         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .utils.maze_grid import get_reachable_neighbours


def create_visited(width: int, height: int) -> list[list[bool]]:
    """Create a grid containing information about visited cells."""
    visited = []

    for y in range(height):
        row = []

        for x in range(width):
            row.append(False)

        visited.append(row)

    return visited


def solve_maze(
    grid: list[list[int]], entry: tuple[int, int], exit: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    BSF algorithm - find the shortest path from entry to exit.
    Link: https://www.redblobgames.com/pathfinding/a-star/introduction.html
    """
    height = len(grid)
    width = len(grid[0])

    visited = create_visited(width, height)

    queue: list[tuple[int, int]] = []
    parent: dict[tuple[int, int], tuple[int, int]] = {}

    entry_x, entry_y = entry

    visited[entry_y][entry_x] = True
    queue.append(entry)

    queue_index = 0
    found = False

    while queue_index < len(queue):
        current = queue[queue_index]
        queue_index += 1

        if current == exit:
            found = True
            break

        neighbours = get_reachable_neighbours(grid, current)

        for neighbour in neighbours:
            x, y = neighbour

            if visited[y][x]:
                continue

            visited[y][x] = True
            parent[neighbour] = current
            queue.append(neighbour)

    if not found:
        raise ValueError("No path from ENTRY to EXIT")

    path = [entry]
    current = exit

    path.append(current)

    while current != entry:
        current = parent[current]
        path.append(current)

    path.reverse()

    return path
