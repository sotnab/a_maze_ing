# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_dfs.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/06 01:02:14 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 21:37:43 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from .maze_algorithm import MazeAlgorithm
from ..types import Cell, Grid, Step


class MazeDfs(MazeAlgorithm):
    """Generate a maze using depth-first search."""

    def __init__(
        self,
        grid: Grid,
        blocked: list[Cell],
        random: Random,
        entry: Cell
    ) -> None:
        """Initialize the DFS maze generator."""

        super().__init__(grid, blocked, random, entry)

    def generate(self) -> list[Step]:
        """
        Generate a perfect maze using iterative DFS.
        Links:
          - https://en.wikipedia.org/wiki/Maze_generation_algorithm
          - https://www.miklix.com/mazes/maze-generators/recursive-backtracker
        """

        self.visited = [[False for _ in range(self.width)]
                        for _ in range(self.height)]

        stack: list[Cell] = []

        start_x, start_y = self.entry

        self.visited[start_y][start_x] = True
        stack.append(self.entry)

        while len(stack) > 0:
            current = stack[-1]

            neighbours = self.get_unvisited_neighbours(current)

            if len(neighbours) == 0:
                stack.pop()
                continue

            next_cell = self.random.choice(neighbours)

            self.open_wall(current, next_cell)

            next_x, next_y = next_cell
            self.visited[next_y][next_x] = True

            stack.append(next_cell)

        return self.steps

    def get_unvisited_neighbours(self, cell: Cell) -> list[Cell]:
        """Return neighbours that have not been visited yet."""
        neighbours = self.get_neighbours(cell)

        def filter_not_visited(cell: Cell) -> bool:
            x, y = cell
            return not self.visited[y][x]

        return list(filter(filter_not_visited, neighbours))
