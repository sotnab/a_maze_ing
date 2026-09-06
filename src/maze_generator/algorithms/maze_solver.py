# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_solver.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/06 13:55:18 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 14:17:37 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ..types import Grid, Cell
from ..constants import (
    NORTH, EAST, SOUTH, WEST
)


class MazeSolver():
    def __init__(self, grid: Grid, entry: Cell, exit: Cell) -> None:

        self.width = len(grid[0])
        self.height = len(grid)

        self.grid = grid
        self.entry = entry
        self.exit = exit

    def solve_maze(self) -> list[Cell]:
        """
        BSF algorithm - find the shortest path from entry to exit.
        Link: https://www.redblobgames.com/pathfinding/a-star/introduction.html
        """
        visited = self.create_visited()

        queue: list[Cell] = []
        parent: dict[Cell, Cell] = {}

        entry_x, entry_y = self.entry

        visited[entry_y][entry_x] = True
        queue.append(self.entry)

        queue_index = 0
        found = False

        while queue_index < len(queue):
            current = queue[queue_index]
            queue_index += 1

            if current == self.exit:
                found = True
                break

            neighbours = self.get_reachable_neighbours(current)

            for neighbour in neighbours:
                x, y = neighbour

                if visited[y][x]:
                    continue

                visited[y][x] = True
                parent[neighbour] = current
                queue.append(neighbour)

        if not found:
            raise ValueError("No path from ENTRY to EXIT")

        return self.create_path(parent)

    def create_path(self, parent: dict[Cell, Cell]) -> list[Cell]:

        path = []
        current = self.exit

        path.append(current)

        while current != self.entry:
            current = parent[current]
            path.append(current)

        path.reverse()

        return path

    def create_visited(self) -> list[list[bool]]:

        return [[False for _ in range(self.width)]
                for _ in range(self.height)]

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

    @staticmethod
    def path_to_directed(path: list[Cell]) -> str:

        directed_path = ""
        last_cell = path[0]

        for cell in path[1:]:

            x1, y1 = last_cell
            x2, y2 = cell

            if y1 > y2:
                directed_path += "N"
            elif y1 < y2:
                directed_path += "S"
            elif x1 > x2:
                directed_path += "W"
            elif x1 < x2:
                directed_path += "E"

            last_cell = cell

        return directed_path
