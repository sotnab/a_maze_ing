# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_prims.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/06 01:12:57 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 14:56:12 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from .maze_algorithm import MazeAlgorithm
from ..types import Cell, Grid, Step


class MazePrims(MazeAlgorithm):
    def __init__(
        self,
        grid: Grid,
        blocked: list[Cell],
        random: Random,
        entry: Cell,
    ) -> None:

        super().__init__(grid, blocked, random, entry)

    def generate(self) -> list[Step]:

        maze_cells = [self.entry]
        unfinished_cells = [self.entry]

        while len(unfinished_cells) > 0:

            cell = self.random.choice(unfinished_cells)

            neighbours = self.get_neighbours_excluding(cell, maze_cells)

            if len(neighbours) == 0:
                unfinished_cells.remove(cell)
                continue

            if self.width == self.height == 3:
                walls = self.number_of_walls(cell)

                if walls < 2:
                    continue

            next_cell = self.random.choice(neighbours)

            self.open_wall(cell, next_cell)

            unfinished_cells.append(next_cell)
            maze_cells.append(next_cell)

        return self.steps

    def get_neighbours_excluding(
            self, cell: Cell, excluded: list[Cell]) -> list[Cell]:

        neighbours = self.get_neighbours(cell)

        return list(filter(lambda cell: cell not in excluded, neighbours))
