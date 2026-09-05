# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  prims.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/04 22:11:11 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 20:48:22 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from ..utils.neighbours import get_neighbours_not_in_maze
from ..utils.maze_grid import open_wall, number_of_walls


def generate_prims(
    grid: list[list[int]],
    entry: tuple[int, int],
    blocked: list[tuple[int, int]],
    random: Random,
) -> list[tuple[int, int, int]]:

    width = len(grid[0])
    height = len(grid)

    steps = []

    maze_cells = [entry]
    unfinished_cells = [entry]

    while len(unfinished_cells) > 0:

        cell = random.choice(unfinished_cells)

        neighbours = get_neighbours_not_in_maze(
            cell, blocked, maze_cells, width, height)

        if len(neighbours) == 0:
            unfinished_cells.remove(cell)
            continue

        x, y = cell

        if width == height == 3 and number_of_walls(grid[y][x]) < 2:
            continue

        next_cell = random.choice(neighbours)

        open_wall(grid, steps, cell, next_cell)

        unfinished_cells.append(next_cell)
        maze_cells.append(next_cell)

    return steps
