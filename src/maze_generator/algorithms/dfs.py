# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  dfs.py                                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/04 22:04:37 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 20:49:11 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from ..utils.maze_grid import open_wall
from ..utils.neighbours import get_unvisited_neighbours


def generate_dfs(
    grid: list[list[int]],
    start: tuple[int, int],
    blocked: list[tuple[int, int]],
    random: Random,
) -> list[tuple[int, int, int]]:
    """
    Generate a perfect maze using iterative DFS.
    Links:
      - https://en.wikipedia.org/wiki/Maze_generation_algorithm
      - https://www.miklix.com/mazes/maze-generators/recursive-backtracker
    """
    height = len(grid)
    width = len(grid[0])

    visited = [[False for _ in range(width)] for _ in range(height)]

    stack: list[tuple[int, int]] = []
    steps: list[tuple[int, int, int]] = []

    start_x, start_y = start

    visited[start_y][start_x] = True
    stack.append(start)

    while len(stack) > 0:
        current = stack[-1]

        neighbours = get_unvisited_neighbours(
            current, visited, blocked, width, height
        )

        if len(neighbours) == 0:
            stack.pop()
            continue

        next_cell = random.choice(neighbours)

        open_wall(grid, steps, current, next_cell)

        next_x, next_y = next_cell
        visited[next_y][next_x] = True

        stack.append(next_cell)

    return steps
