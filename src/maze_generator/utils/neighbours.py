# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  neighbours.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/04 22:09:19 by wbaran          #+#    #+#               #
#  Updated: 2026/09/04 22:44:37 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def get_neighbours(
    current: tuple[int, int],
    blocked: list[tuple[int, int]],
    width: int,
    height: int,
) -> list[tuple[int, int]]:

    x, y = current
    neighbours = []

    possible = [
        (x, y - 1),  # North
        (x + 1, y),  # East
        (x, y + 1),  # South
        (x - 1, y),  # West
    ]

    for cell in possible:
        x, y = cell

        if 0 <= x < width and 0 <= y < height:

            if cell not in blocked:
                neighbours.append(cell)

    return neighbours


def get_unvisited_neighbours(
    current: tuple[int, int],
    visited: list[list[bool]],
    blocked: list[tuple[int, int]],
    width: int,
    height: int,
) -> list[tuple[int, int]]:
    """Return unvisited and non-blocked neighbours."""

    neighbours = get_neighbours(current, blocked, width, height)

    unvisited = list(filter(
        lambda cell: not visited[cell[1]][cell[0]], neighbours))

    return unvisited


def get_neighbours_excluding(
    current: tuple[int, int],
    excluded: tuple[int, int] | None,
    blocked: list[tuple[int, int]],
    width: int,
    height: int,
) -> list[tuple[int, int]]:
    """Return unvisited and non-blocked neighbours."""

    neighbours = get_neighbours(current, blocked, width, height)

    result = list(filter(
        lambda cell: cell != excluded, neighbours))

    return result


def get_neighbours_not_in_maze(
    current: tuple[int, int],
    blocked: list[tuple[int, int]],
    maze: list[tuple[int, int]],
    width: int,
    height: int,
) -> list[tuple[int, int]]:
    """Return unvisited and non-blocked neighbours."""

    neighbours = get_neighbours(current, blocked, width, height)

    result = list(filter(
        lambda cell: cell not in maze, neighbours))

    return result
