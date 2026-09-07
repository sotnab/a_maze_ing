# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  wall_drawer.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/14 00:39:51 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 21:37:43 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray
from itertools import cycle

from .drawer import Drawer
from ..constants import (
    WALL_COLORS,
    PATTERN_COLOR,
    ENTRY_COLOR,
    EXIT_COLOR
)

from maze_gen import Cell


class WallDrawer(Drawer):
    """Draw maze walls and special cells such as entry and exit."""

    def __init__(
            self, pixels: ndarray,
            cell_size: tuple[int, int]
    ) -> None:
        """Initialize the wall drawer and palette."""
        super().__init__(pixels, cell_size)

        self.wall_colors = cycle(WALL_COLORS)

        self.wall_color = next(self.wall_colors)
        self.pattern_color = PATTERN_COLOR

    def set_cell_size(self, cell_size: tuple[int, int]) -> None:
        """Set the cell size and compute the wall thickness."""
        super().set_cell_size(cell_size)
        self.wall_width = self.get_wall_width()

    def draw_walls(
            self, walls: int,
            cell: Cell,
            complete: bool = False,
            entry: bool = False,
            exit: bool = False
    ) -> None:
        """Draw the walls for one cell, plus optional colors."""

        if not complete and walls == 15:
            return

        if complete and walls == 15:
            self.draw_colored_cell(cell, self.pattern_color)

        if complete and entry:
            self.draw_colored_cell(cell, ENTRY_COLOR)

        if complete and exit:
            self.draw_colored_cell(cell, EXIT_COLOR)

        if walls & 1 == 1:
            self.draw_top_wall(cell)

        if (walls >> 1) & 1 == 1:
            self.draw_right_wall(cell)

        if (walls >> 2) & 1 == 1:
            self.draw_bottom_wall(cell)

        if (walls >> 3) & 1 == 1:
            self.draw_left_wall(cell)

    def draw_top_wall(self, cell: Cell) -> None:
        """Draw the north wall of a cell."""
        x, y = self.cell_coords(cell)

        end_y = y + self.wall_width
        end_x = x + self.cell_width

        self.pixels[y:end_y, x:end_x] = self.wall_color

    def draw_right_wall(self, cell: Cell) -> None:
        """Draw the east wall of a cell."""
        x, y = self.cell_coords(cell)

        end_y = y + self.cell_height
        start_x = x + self.cell_width - self.wall_width
        end_x = x + self.cell_width

        self.pixels[y:end_y, start_x:end_x] = self.wall_color

    def draw_bottom_wall(self, cell: Cell) -> None:
        """Draw the south wall of a cell."""
        x, y = self.cell_coords(cell)

        start_y = y + self.cell_height - self.wall_width
        end_y = y + self.cell_height
        end_x = x + self.cell_width

        self.pixels[start_y:end_y, x:end_x] = self.wall_color

    def draw_left_wall(self, cell: Cell) -> None:
        """Draw the west wall of a cell."""
        x, y = self.cell_coords(cell)

        end_y = y + self.cell_height
        end_x = x + self.wall_width

        self.pixels[y:end_y, x:end_x] = self.wall_color

    def draw_colored_cell(self, cell: Cell, color: int) -> None:
        """Fill a cell with a solid color."""
        x, y = self.cell_coords(cell)

        padding = self.wall_width

        start_y = y + padding
        start_x = x + padding

        end_y = y + self.cell_height - padding
        end_x = x + self.cell_width - padding

        self.pixels[start_y:end_y, start_x:end_x] = color

    def clear_cell(self, cell: Cell) -> None:
        """Clear the pixels for one cell."""

        x, y = self.cell_coords(cell)

        end_y = y + self.cell_height
        end_x = x + self.cell_width

        self.pixels[y:end_y, x:end_x] = 0

    def switch_colors(self) -> None:
        """Rotate to the next wall color."""
        self.wall_color = next(self.wall_colors)

    def get_wall_width(self) -> int:
        """Return the current wall thickness based on cell size."""

        min_dimension = min((self.cell_width, self.cell_height))

        if min_dimension < 20:
            return 1
        if min_dimension < 80:
            return 2
        if min_dimension < 120:
            return 6
        else:
            return 12
