# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_gen.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/22 15:14:13 by wbaran          #+#    #+#               #
#  Updated: 2026/09/04 20:32:40 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random
from typing import TypeVar

from .maze import Maze
from .maze_solver import solve_maze
from .pattern_42 import get_42_cells
from src.maze_config import MazeConfig, Algorithm
from .maze_grid import (
    create_grid,
    grid_to_hex,
    open_wall,
    close_wall,
    number_of_walls
)


T = TypeVar("T")


def add_steps(
    steps: list[tuple[int, int, int]],
    grid: list[list[int]],
    cell1: tuple[int, int],
    cell2: tuple[int, int]
) -> None:

    x1, y1 = cell1
    x2, y2 = cell2

    steps.append((x1, y1, grid[y1][x1]))
    steps.append((x2, y2, grid[y2][x2]))


def create_visited(width: int, height: int) -> list[list[bool]]:
    """Create visited grid initialized to False."""

    return [[False for _ in range(width)] for _ in range(height)]


def get_unvisited_neighbours(
    current: tuple[int, int],
    visited: list[list[bool]],
    blocked: list[tuple[int, int]],
    width: int,
    height: int,
) -> list[tuple[int, int]]:
    """Return unvisited and non-blocked neighbours."""
    x, y = current
    neighbours = []

    # North
    if y > 0:
        next_cell = (x, y - 1)

        if next_cell not in blocked:
            if not visited[y - 1][x]:
                neighbours.append(next_cell)

    # East
    if x < width - 1:
        next_cell = (x + 1, y)

        if next_cell not in blocked:
            if not visited[y][x + 1]:
                neighbours.append(next_cell)

    # South
    if y < height - 1:
        next_cell = (x, y + 1)

        if next_cell not in blocked:
            if not visited[y + 1][x]:
                neighbours.append(next_cell)

    # West
    if x > 0:
        next_cell = (x - 1, y)

        if next_cell not in blocked:
            if not visited[y][x - 1]:
                neighbours.append(next_cell)

    return neighbours


def get_neighbours_excluding(
    current: tuple[int, int],
    excluded: tuple[int, int] | None,
    blocked: list[tuple[int, int]],
    width: int,
    height: int,
) -> list[tuple[int, int]]:
    """Return unvisited and non-blocked neighbours."""
    x, y = current
    neighbours = []

    possible_cells = [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y)
    ]

    for cell in possible_cells:
        x, y = cell

        if 0 <= x < width and 0 <= y < height:
            if cell not in blocked and cell != excluded:
                neighbours.append(cell)

    return neighbours


def generate_dfs(
    grid: list[list[int]],
    start: tuple[int, int],
    blocked: list[tuple[int, int]],
    random: Random,
) -> list[tuple[int, int, int]]:
    """
    Generate a perfect maze using iterative DFS.
    Links:
      - https://en.wikipedia.org/wiki/Maze_generation_algorithm
      - https://www.miklix.com/mazes/maze-generators/recursive-backtracker
    """
    height = len(grid)
    width = len(grid[0])

    visited = create_visited(width, height)
    stack: list[tuple[int, int]] = []
    steps: list[tuple[int, int, int]] = []

    start_x, start_y = start

    visited[start_y][start_x] = True
    stack.append(start)

    while len(stack) > 0:
        current = stack[-1]

        neighbours = get_unvisited_neighbours(
            current, visited, blocked, width, height
        )

        if len(neighbours) == 0:
            stack.pop()
            continue

        next_cell = random.choice(neighbours)

        open_wall(grid, current, next_cell)

        add_steps(steps, grid, current, next_cell)

        next_x, next_y = next_cell
        visited[next_y][next_x] = True

        stack.append(next_cell)

    return steps


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


def remove_dead_ends(
    grid: list[list[int]],
    blocked: list[tuple[int, int]]
) -> list[tuple[int, int, int]]:

    width = len(grid[0])
    height = len(grid)

    visited = [[False] * width] * height

    dead_ends: list[tuple[int, int]] = []
    steps: list[tuple[int, int, int]] = []

    for y, row in enumerate(grid):
        for x, walls in enumerate(row):
            cell = (x, y)

            if number_of_walls(walls) == 3:
                dead_ends.append(cell)

    while len(dead_ends):
        cell = dead_ends.pop()

        neighbours = get_unvisited_neighbours(
            cell, visited, blocked, width, height
        )

        for neighbour in neighbours:
            x1, y1 = cell

            if number_of_walls(grid[y1][x1]) == 3:
                open_wall(grid, cell, neighbour)

                add_steps(steps, grid, cell, neighbour)

    return steps


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
