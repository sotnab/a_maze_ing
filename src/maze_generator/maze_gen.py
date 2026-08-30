# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_gen.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/22 15:14:13 by wbaran          #+#    #+#               #
#  Updated: 2026/08/22 17:14:04 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from random import Random

from .maze import Maze
from .maze_grid import create_grid, grid_to_hex, open_wall
from .pattern_42 import get_42_cells
from src.maze_config import MazeConfig


def create_visited(width: int, height: int) -> list[list[bool]]:
    """Create visited grid initialized to False."""
    visited = []

    for y in range(height):
        row = []

        for x in range(width):
            row.append(False)

        visited.append(row)

    return visited


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


def generate_dfs(
    grid: list[list[int]],
    start: tuple[int, int],
    blocked: list[tuple[int, int]],
    random: Random,
) -> None:
    """Generate a perfect maze using iterative DFS."""
    height = len(grid)
    width = len(grid[0])

    visited = create_visited(width, height)
    stack = []

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

        next_x, next_y = next_cell
        visited[next_y][next_x] = True

        stack.append(next_cell)


class MazeGen:
    def __init__(self, config: MazeConfig) -> None:
        self.config = config
        self.random = Random(config.seed)

    def generate(self) -> Maze:
        grid = create_grid(self.config.width, self.config.height)

        blocked = get_42_cells(
            self.config.width,
            self.config.height,
            self.config.entry,
            self.config.exit,
        )

        generate_dfs(grid, self.config.entry, blocked, self.random)

        data = grid_to_hex(grid)

        maze = Maze(
            data,
            self.config.width,
            self.config.height,
            self.config.entry,
            self.config.exit,
        )

        return maze
