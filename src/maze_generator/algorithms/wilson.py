# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  wilson.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/04 22:14:06 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 19:44:14 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from ..utils.maze_grid import open_wall, close_wall
from ..utils.neighbours import get_neighbours_excluding
from ..utils.steps import add_steps


def wilson_exit_dead_end(
    path: list[tuple[int, int]],
    blocked: list[tuple[int, int]],
    width: int,
    height: int,
    steps: list[tuple[int, int, int]],
    grid: list[list[int]]
) -> None:

    while len(path) > 1:

        last = path.pop()
        current = path[-1]

        close_wall(grid, last, current)
        add_steps(steps, grid, last, current)

        neighbours = get_neighbours_excluding(
            last, current, blocked, width, height)

        if len(neighbours) > 1:
            return


def wilson_erase_loop(
    path: list[tuple[int, int]],
    cell: tuple[int, int],
    steps: list[tuple[int, int, int]],
    grid: list[list[int]]
) -> None:

    while True:
        last = path.pop()
        current = path[-1]

        close_wall(grid, last, current)
        add_steps(steps, grid, last, current)

        if path[-1] == cell:
            return


def generate_wilson(
    grid: list[list[int]],
    exit: tuple[int, int],
    blocked: list[tuple[int, int]],
    random: Random,
) -> list[tuple[int, int, int]]:

    width = len(grid[0])
    height = len(grid)

    steps: list[tuple[int, int, int]] = []

    empty_cells = [(x, y) for x in range(width) for y in range(height)]

    for cell in blocked:
        empty_cells.remove(cell)

    empty_cells.remove(exit)

    while len(empty_cells) > 0:

        path = []

        path.append(random.choice(empty_cells))

        while True:
            cell = path[-1]

            previous_cell = path[-2] if len(path) > 1 else None

            neighbours = get_neighbours_excluding(
                cell, previous_cell, blocked, width, height)

            if len(neighbours) == 0:
                wilson_exit_dead_end(path, blocked, width, height, steps, grid)
                continue

            next_cell = random.choice(neighbours)

            if next_cell in path:
                wilson_erase_loop(path, next_cell, steps, grid)
                continue

            path.append(next_cell)
            open_wall(grid, cell, next_cell)

            add_steps(steps, grid, cell, next_cell)

            if next_cell not in empty_cells:
                break

        for cell in path[:-1]:
            empty_cells.remove(cell)

    return steps
