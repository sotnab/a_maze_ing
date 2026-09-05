# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  not_perfect.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/04 22:16:07 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 20:48:10 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..utils.neighbours import get_neighbours
from ..utils.maze_grid import open_wall, number_of_walls


def remove_dead_ends(
    grid: list[list[int]],
    blocked: list[tuple[int, int]]
) -> list[tuple[int, int, int]]:

    width = len(grid[0])
    height = len(grid)

    dead_ends: list[tuple[int, int]] = []
    steps: list[tuple[int, int, int]] = []

    for y, row in enumerate(grid):
        for x, walls in enumerate(row):
            cell = (x, y)

            if number_of_walls(walls) == 3:
                dead_ends.append(cell)

    while len(dead_ends):
        cell = dead_ends.pop()

        neighbours = get_neighbours(
            cell, blocked, width, height
        )

        for neighbour in neighbours:
            x1, y1 = cell

            if number_of_walls(grid[y1][x1]) == 3:
                open_wall(grid, steps, cell, neighbour)

    return steps
