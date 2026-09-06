# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_wilson.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/06 00:43:27 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 15:33:47 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from .maze_algorithm import MazeAlgorithm
from ..types import Cell, Grid, Step


class MazeWilson(MazeAlgorithm):
    def __init__(
        self,
        grid: Grid,
        blocked: list[Cell],
        random: Random,
        entry: Cell
    ) -> None:

        super().__init__(grid, blocked, random, entry)

    def generate(self) -> list[Step]:

        empty_cells = [(x, y) for x in range(self.width)
                       for y in range(self.height)]

        for cell in self.blocked:
            empty_cells.remove(cell)

        empty_cells.remove(self.entry)

        while len(empty_cells) > 0:

            path = []
            path.append(self.random.choice(empty_cells))

            while True:

                cell = path[-1]
                previous_cell = path[-2] if len(path) > 1 else None

                neighbours = self.get_neighbours_excluding(cell, previous_cell)

                if len(neighbours) == 0:
                    self.exit_dead_end(path)
                    continue

                next_cell = self.random.choice(neighbours)

                if next_cell in path:
                    self.erase_loop(path, next_cell)
                    continue

                path.append(next_cell)
                self.open_wall(cell, next_cell)

                if next_cell not in empty_cells:
                    break

            for cell in path[:-1]:
                empty_cells.remove(cell)

        return self.steps

    def exit_dead_end(self, path: list[Cell]) -> None:

        while len(path) > 1:

            last = path.pop()
            current = path[-1]

            self.close_wall(last, current)

            neighbours = self.get_neighbours_excluding(last, current)

            if len(neighbours) > 1:
                return

    def erase_loop(self, path: list[Cell], cell: Cell) -> None:

        while True:
            last = path.pop()
            current = path[-1]

            self.close_wall(last, current)

            if path[-1] == cell:
                return

    def get_neighbours_excluding(
            self, cell: Cell, excluded: Cell | None) -> list[Cell]:

        neighbours = self.get_neighbours(cell)

        return list(filter(lambda cell: cell != excluded, neighbours))
