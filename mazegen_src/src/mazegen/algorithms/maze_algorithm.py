# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_algorithm.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/05 23:45:16 by wbaran          #+#    #+#               #
#  Updated: 2026/09/17 16:14:05 by wbaran          ###   ########.fr        #
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
    """Base class for maze generation algorithms."""

    def __init__(
            self,
            grid: Grid,
            blocked: list[Cell],
            random: Random,
            entry: Cell
    ) -> None:
        """Initialize the algorithm state."""

        self.grid = grid
        self.blocked = blocked
        self.random = random
        self.entry = entry

        self.width = len(grid[0])
        self.height = len(grid)

        self.steps: list[Step] = []

    @abstractmethod
    def generate(self) -> list[Step]:
        """Generate the maze and return the step list."""
        ...

    def get_neighbours(self, cell: Cell) -> list[Cell]:
        """Return valid cells adjacent to the current cell."""

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

    def get_reachable_neighbours(self, cell: Cell) -> list[Cell]:
        """Return cells reachable from the current cell."""
        x, y = cell
        walls = self.grid[y][x]

        neighbours = []

        # North
        if y > 0:
            if (walls & NORTH) == 0:
                neighbours.append((x, y - 1))

        # East
        if x < self.width - 1:
            if (walls & EAST) == 0:
                neighbours.append((x + 1, y))

        # South
        if y < self.height - 1:
            if (walls & SOUTH) == 0:
                neighbours.append((x, y + 1))

        # West
        if x > 0:
            if (walls & WEST) == 0:
                neighbours.append((x - 1, y))

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
        """Close the wall between two neighbouring cells."""
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
        """Remove dead ends from the generated maze."""

        dead_ends: list[Cell] = []

        for y in range(self.height):
            for x in range(self.width):
                cell = (x, y)

                if self.number_of_walls(cell) == 3:
                    dead_ends.append(cell)

        while len(dead_ends):
            cell = self.random.choice(dead_ends)

            dead_ends.remove(cell)

            neighbours = self.get_neighbours(cell)

            for neighbour in neighbours:

                if self.number_of_walls(cell) == 3:
                    self.open_wall(cell, neighbour)

        if self.width == 3 or self.height == 3:
            self.fix_open_areas()

        return self.steps

    def fix_open_areas(self) -> None:

        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):

                if self.number_of_walls((x, y)) != 0:
                    continue

                neighbours = [
                    (x, y - 1), (x + 1, y),
                    (x, y + 1), (x - 1, y)
                ]

                neighbours_diagonally = [
                    (x - 1, y - 1), (x + 1, y - 1),
                    (x - 1, y + 1), (x + 1, y + 1)
                ]

                if any(self.number_of_walls(neighbour) != 1
                        for neighbour in neighbours):
                    continue

                if any(self.number_of_walls(neighbour) != 2
                        for neighbour in neighbours_diagonally):
                    continue

                self.close_wall((x, y), self.random.choice(neighbours))

    def independent_loops(self) -> int:

        connections = 0

        for y in range(self.height):
            for x in range(self.width):
                cell = (x, y)

                neighbours = self.get_reachable_neighbours(cell)

                for neighbour in neighbours:
                    if neighbour > cell:
                        connections += 1

        total_cells = (self.height * self.width) - len(self.blocked)

        independent_loops = connections - total_cells + 1

        return independent_loops

    def number_of_walls(self, cell: Cell) -> int:
        """Count the number of walls still present in a cell."""
        count = 0
        x, y = cell

        for direction in [NORTH, EAST, SOUTH, WEST]:
            if self.grid[y][x] & direction > 0:
                count += 1

        return count
