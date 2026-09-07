# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_gen.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/22 15:14:13 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 16:21:04 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random
from sys import stderr

from .maze import Maze
from .config.maze_config import MazeConfig

from .algorithms.maze_algorithm import MazeAlgorithm
from .algorithms.maze_dfs import MazeDfs
from .algorithms.maze_wilson import MazeWilson
from .algorithms.maze_prims import MazePrims
from .algorithms.maze_solver import MazeSolver

from .types import MazeData, Cell, Grid
from .constants import (
    NORTH, EAST, SOUTH, WEST, ALL_WALLS,
    PATTERN_42
)


class MazeGen:
    def dfs(self, config: MazeConfig) -> Maze:
        return self.generate(MazeDfs, config)

    def wilson(self, config: MazeConfig) -> Maze:
        return self.generate(MazeWilson, config)

    def prims(self, config: MazeConfig) -> Maze:
        return self.generate(MazePrims, config)

    def generate(
        self,
        maze_algorithm: type[MazeAlgorithm],
        config: MazeConfig
    ) -> Maze:

        random = Random(config.seed)
        grid = self.create_grid(config.width, config.height)
        blocked = self.get_42_cells(config)
        algorithm = maze_algorithm(grid, blocked, random, config.entry)

        steps = algorithm.generate()

        if not config.perfect:
            steps = algorithm.remove_dead_ends()

        solver = MazeSolver(grid, config.entry, config.exit)

        solution = solver.solve_maze()

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

        return maze

    def save_to_file(self, maze: Maze, filename: str) -> None:

        with open(filename, "w") as out_file:

            for line in maze.data:
                out_file.write(line + "\n")

            out_file.write("\n")

            out_file.write(",".join(map(str, maze.entry)) + "\n")
            out_file.write(",".join(map(str, maze.exit)) + "\n")

            out_file.write(MazeSolver.path_to_directed(maze.solution) + "\n")

    def number_of_walls(self, walls: int) -> int:
        count = 0

        for direction in [NORTH, EAST, SOUTH, WEST]:
            if walls & direction > 0:
                count += 1

        return count

    def create_grid(self, width: int, height: int) -> Grid:

        return [[ALL_WALLS for _ in range(width)] for _ in range(height)]

    def grid_to_hex(self, grid: Grid) -> MazeData:
        """Convert the grid to hexadecimal rows."""
        result = []

        for row in grid:
            hex_row = ""

            for cell in row:
                hex_row += format(cell, "X")

            result.append(hex_row)

        return result

    def get_42_cells(self, config: MazeConfig) -> list[Cell]:
        """Return cells used to draw the 42 pattern."""

        pattern_height = len(PATTERN_42)
        pattern_width = len(PATTERN_42[0])

        if config.width < pattern_width + 2:
            print("Maze is too small for the 42 pattern", file=stderr)
            return []

        if config.height < pattern_height + 2:
            print("Maze is too small for the 42 pattern", file=stderr)
            return []

        start_x = (config.width // 2) - (pattern_width // 2)
        start_y = (config.height // 2) - (pattern_height // 2)

        for y in range(start_y, config.height - pattern_height):
            for x in range(start_x, config.width - pattern_width):
                cells = []
                valid_position = True

                for row in range(pattern_height):
                    for col in range(pattern_width):
                        if PATTERN_42[row][col] != "X":
                            continue

                        x = start_x + col
                        y = start_y + row
                        cell = (x, y)

                        if cell == config.entry or cell == config.exit:
                            valid_position = False

                        cells.append(cell)

                if valid_position:
                    return cells

        print("Cannot place the 42 pattern", file=stderr)
        return []
