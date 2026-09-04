# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_gen.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/22 15:14:13 by wbaran          #+#    #+#               #
#  Updated: 2026/09/04 22:24:16 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from .maze import Maze
from .maze_solver import solve_maze
from .utils.pattern_42 import get_42_cells
from src.maze_config import MazeConfig, Algorithm
from .algorithms.dfs import generate_dfs
from .algorithms.wilson import generate_wilson
from .algorithms.prims import generate_prims
from .algorithms.not_perfect import remove_dead_ends
from .utils.maze_grid import (
    create_grid,
    grid_to_hex
)


class MazeGen:
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file

    def generate(self) -> Maze:
        self.config = MazeConfig.from_file(self.config_file)
        self.random = Random(self.config.seed)

        grid = create_grid(self.config.width, self.config.height)

        blocked = get_42_cells(
            self.config.width,
            self.config.height,
            self.config.entry,
            self.config.exit,
        )

        steps = []

        if self.config.algorithm == Algorithm.DFS:
            steps.extend(
                generate_dfs(grid, self.config.entry, blocked, self.random)
            )

        if self.config.algorithm == Algorithm.WILSON:
            steps.extend(
                generate_wilson(grid, self.config.exit, blocked, self.random)
            )

        if self.config.algorithm == Algorithm.PRIMS:
            steps.extend(
                generate_prims(grid, self.config.entry, blocked, self.random)
            )

        if not self.config.perfect:
            steps.extend(remove_dead_ends(grid, blocked))

        steps.reverse()

        solution = solve_maze(grid, self.config.entry, self.config.exit)

        data = grid_to_hex(grid)

        maze = Maze(
            data,
            self.config.width,
            self.config.height,
            self.config.entry,
            self.config.exit,
            solution,
            steps
        )

        self.save_to_file(maze, self.config.output_file)

        return maze

    def save_to_file(self, maze: Maze, filename: str) -> None:

        with open(filename, "w") as out_file:

            for line in maze.data:
                out_file.write(line + "\n")

            out_file.write("\n")

            x1, y1 = self.config.entry
            x2, y2 = self.config.exit

            out_file.write(str(x1) + "," + str(y1) + "\n")
            out_file.write(str(x2) + "," + str(y2) + "\n")

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
