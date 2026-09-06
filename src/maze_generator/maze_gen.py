# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_gen.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/22 15:14:13 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 02:01:36 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from .maze import Maze
from .maze_solver import solve_maze
from .pattern_42 import get_42_cells
from .config.maze_config import MazeConfig

from .algorithms.maze_algorithm import MazeAlgorithm
from .algorithms.maze_dfs import MazeDfs
from .algorithms.maze_wilson import MazeWilson
from .algorithms.maze_prims import MazePrims

from .types import Grid
from .constants import NORTH, EAST, SOUTH, WEST, ALL_WALLS


class MazeGen:
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file

    def dfs(self) -> Maze:
        return self.generate(MazeDfs)

    def wilson(self) -> Maze:
        return self.generate(MazeWilson)

    def prims(self) -> Maze:
        return self.generate(MazePrims)

    def generate(self, maze_algorithm: type[MazeAlgorithm]) -> Maze:
        config = MazeConfig.from_file(self.config_file)

        random = Random(config.seed)

        grid = self.create_grid(config.width, config.height)

        blocked = get_42_cells(
            config.width,
            config.height,
            config.entry,
            config.exit,
        )

        algorithm = maze_algorithm(grid, blocked, random, config.entry)

        steps = algorithm.generate()

        if not config.perfect:
            steps = algorithm.remove_dead_ends()

        solution = solve_maze(grid, config.entry, config.exit)

        data = self.grid_to_hex(grid)

        maze = Maze(
            data,
            config.width,
            config.height,
            config.entry,
            config.exit,
            solution,
            steps
        )

        self.save_to_file(maze, config.output_file)

        return maze

    def save_to_file(self, maze: Maze, filename: str) -> None:

        with open(filename, "w") as out_file:

            for line in maze.data:
                out_file.write(line + "\n")

            out_file.write("\n")

            out_file.write(",".join(map(str, maze.entry)) + "\n")
            out_file.write(",".join(map(str, maze.exit)) + "\n")

            out_file.write(self.path_directed(maze.solution) + "\n")

    def path_directed(self, path: list[tuple[int, int]]) -> str:

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

    def number_of_walls(self, walls: int) -> int:
        count = 0

        for direction in [NORTH, EAST, SOUTH, WEST]:
            if walls & direction > 0:
                count += 1

        return count

    def create_grid(self, width: int, height: int) -> list[list[int]]:

        return [[ALL_WALLS for _ in range(width)] for _ in range(height)]

    def grid_to_hex(self, grid: Grid) -> list[str]:
        """Convert the grid to hexadecimal rows."""
        result = []

        for row in grid:
            hex_row = ""

            for cell in row:
                hex_row += format(cell, "X")

            result.append(hex_row)

        return result
