# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    pattern_42.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: jazurek <jazurek@student.42.pl>           +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/08/24 21:17:46 by jazurek          #+#    #+#              #
#    Updated: 2026/08/30 01:03:21 by jazurek         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from sys import stderr

from .constants import PATTERN_42


def get_42_cells(
    width: int, height: int, entry: tuple[int, int], exit: tuple[int, int]
) -> list[tuple[int, int]]:
    """Return cells used to draw the 42 pattern."""
    pattern_height = len(PATTERN_42)
    pattern_width = len(PATTERN_42[0])

    if width < pattern_width + 2:
        print("Maze is too small for the 42 pattern", file=stderr)
        return []

    if height < pattern_height + 2:
        print("Maze is too small for the 42 pattern", file=stderr)
        return []

    pattern_start_x = (width // 2) - (pattern_width // 2)
    pattern_start_y = (height // 2) - (pattern_height // 2)

    for start_y in range(pattern_start_y, height - pattern_height):
        for start_x in range(pattern_start_x, width - pattern_width):
            cells = []
            valid_position = True

            for row in range(pattern_height):
                for col in range(pattern_width):
                    if PATTERN_42[row][col] != "X":
                        continue

                    x = start_x + col
                    y = start_y + row
                    cell = (x, y)

                    if cell == entry or cell == exit:
                        valid_position = False

                    cells.append(cell)

            if valid_position:
                return cells

    print("Cannot place the 42 pattern", file=stderr)
    return []
