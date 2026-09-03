# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    maze_grid.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jazurek <jazurek@student.42.pl>           +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/16 20:20:25 by jazurek          #+#    #+#              #
#    Updated: 2026/08/30 21:30:20 by jazurek         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from .constants import (
    NORTH, EAST,
    SOUTH, WEST,
    ALL_WALLS,
    REMOVE_NORTH,
    REMOVE_EAST,
    REMOVE_SOUTH,
    REMOVE_WEST
)


def create_grid(width: int, height: int) -> list[list[int]]:
    """Create a maze with all walls closed."""
    grid = []

    for y in range(height):
        row = []

        for x in range(width):
            row.append(ALL_WALLS)

        grid.append(row)

    return grid


def open_wall(
    grid: list[list[int]], first: tuple[int, int], second: tuple[int, int]
) -> None:
    """Open the wall between two neighbouring cells."""
    x1, y1 = first
    x2, y2 = second

    if x2 == x1 + 1 and y2 == y1:
        grid[y1][x1] &= REMOVE_EAST
        grid[y2][x2] &= REMOVE_WEST

    elif x2 == x1 - 1 and y2 == y1:
        grid[y1][x1] &= REMOVE_WEST
        grid[y2][x2] &= REMOVE_EAST

    elif y2 == y1 + 1 and x2 == x1:
        grid[y1][x1] &= REMOVE_SOUTH
        grid[y2][x2] &= REMOVE_NORTH

    elif y2 == y1 - 1 and x2 == x1:
        grid[y1][x1] &= REMOVE_NORTH
        grid[y2][x2] &= REMOVE_SOUTH

    else:
        raise ValueError("Cells are not neighbours")


def grid_to_hex(grid: list[list[int]]) -> list[str]:
    """Convert the grid to hexadecimal rows."""
    result = []

    for row in grid:
        hex_row = ""

        for cell in row:
            hex_row += format(cell, "X")

        result.append(hex_row)

    return result


def get_reachable_neighbours(
    grid: list[list[int]], cell: tuple[int, int]
) -> list[tuple[int, int]]:
    """Return cells reachable from the current cell."""
    x, y = cell
    height = len(grid)
    width = len(grid[0])
    walls = grid[y][x]

    neighbours = []

    # North
    if y > 0:
        if (walls & NORTH) == 0:
            neighbours.append((x, y - 1))

    # East
    if x < width - 1:
        if (walls & EAST) == 0:
            neighbours.append((x + 1, y))

    # South
    if y < height - 1:
        if (walls & SOUTH) == 0:
            neighbours.append((x, y + 1))

    # West
    if x > 0:
        if (walls & WEST) == 0:
            neighbours.append((x - 1, y))

    return neighbours
