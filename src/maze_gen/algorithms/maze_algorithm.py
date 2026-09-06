# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_algorithm.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/05 23:45:16 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 01:49:57 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random
from abc import ABC, abstractmethod

from ..types import (
    Cell, Grid, Step
)

from ..constants import (
    REMOVE_NORTH,
    REMOVE_WEST,
    REMOVE_SOUTH,
    REMOVE_EAST,
    NORTH, WEST,
    SOUTH, EAST
)


class MazeAlgorithm(ABC):

    def __init__(
            self,
            grid: Grid,
            blocked: list[Cell],
            random: Random,
            entry: Cell
    ) -> None:

        self.grid = grid
        self.blocked = blocked
        self.random = random
        self.entry = entry

        self.width = len(grid[0])
        self.height = len(grid)

        self.steps: list[Step] = []

    @abstractmethod
    def generate(self) -> list[Step]:
        ...

    def get_neighbours(self, cell: Cell) -> list[Cell]:

        neighbours: list[Cell] = []

        x, y = cell

        possible_cells = [
            (x, y - 1),  # North
            (x + 1, y),  # East
            (x, y + 1),  # South
            (x - 1, y),  # West
        ]

        for item in possible_cells:

            if item not in self.blocked:
                x, y = item

                if 0 <= x < self.width and 0 <= y < self.height:
                    neighbours.append(item)

        return neighbours

    def open_wall(self, first: Cell, second: Cell) -> None:
        """Open the wall between two neighbouring cells."""
        x1, y1 = first
        x2, y2 = second

        if x2 == x1 + 1 and y2 == y1:
            self.grid[y1][x1] &= REMOVE_EAST
            self.grid[y2][x2] &= REMOVE_WEST

        elif x2 == x1 - 1 and y2 == y1:
            self.grid[y1][x1] &= REMOVE_WEST
            self.grid[y2][x2] &= REMOVE_EAST

        elif y2 == y1 + 1 and x2 == x1:
            self.grid[y1][x1] &= REMOVE_SOUTH
            self.grid[y2][x2] &= REMOVE_NORTH

        elif y2 == y1 - 1 and x2 == x1:
            self.grid[y1][x1] &= REMOVE_NORTH
            self.grid[y2][x2] &= REMOVE_SOUTH

        else:
            raise ValueError("Cells are not neighbours")

        self.steps.append((x1, y1, self.grid[y1][x1]))
        self.steps.append((x2, y2, self.grid[y2][x2]))

    def close_wall(self, first: Cell, second: Cell) -> None:
        """Open the wall between two neighbouring cells."""
        x1, y1 = first
        x2, y2 = second

        if x2 == x1 + 1 and y2 == y1:
            self.grid[y1][x1] |= EAST
            self.grid[y2][x2] |= WEST

        elif x2 == x1 - 1 and y2 == y1:
            self.grid[y1][x1] |= WEST
            self.grid[y2][x2] |= EAST

        elif y2 == y1 + 1 and x2 == x1:
            self.grid[y1][x1] |= SOUTH
            self.grid[y2][x2] |= NORTH

        elif y2 == y1 - 1 and x2 == x1:
            self.grid[y1][x1] |= NORTH
            self.grid[y2][x2] |= SOUTH

        else:
            raise ValueError("Cells are not neighbours")

        self.steps.append((x1, y1, self.grid[y1][x1]))
        self.steps.append((x2, y2, self.grid[y2][x2]))

    def remove_dead_ends(self) -> list[Step]:

        dead_ends: list[Cell] = []

        for y in range(self.height):
            for x in range(self.width):
                cell = (x, y)

                if self.number_of_walls(cell) == 3:
                    dead_ends.append(cell)

        while len(dead_ends):
            cell = dead_ends.pop()

            neighbours = self.get_neighbours(cell)

            for neighbour in neighbours:

                if self.number_of_walls(cell) == 3:
                    self.open_wall(cell, neighbour)

        return self.steps

    def number_of_walls(self, cell: Cell) -> int:
        count = 0
        x, y = cell

        for direction in [NORTH, EAST, SOUTH, WEST]:
            if self.grid[y][x] & direction > 0:
                count += 1

        return count
