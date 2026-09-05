# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  wall_drawer.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/14 00:39:51 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 23:09:38 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray
from itertools import cycle

from .drawer import Drawer
from .constants import (
    WALL_COLORS,
    PATTERN_COLOR,
    ENTRY_COLOR,
    EXIT_COLOR
)


class WallDrawer(Drawer):
    def __init__(
            self, pixels: ndarray,
            cell_size: tuple[int, int]
    ) -> None:
        super().__init__(pixels, cell_size)

        self.set_cell_size(cell_size)

        self.wall_colors = cycle(WALL_COLORS)

        self.wall_color = next(self.wall_colors)
        self.pattern_color = PATTERN_COLOR

    def set_cell_size(self, cell_size: tuple[int, int]) -> None:

        self.cell_size = cell_size
        self.wall_width = self.get_wall_width(cell_size)

    def draw_walls(
            self, walls: int,
            cell: tuple[int, int],
            complete: bool = False,
            entry: bool = False,
            exit: bool = False
    ) -> None:

        x, y = self.cell_coords(cell)

        if not complete and walls == 15:
            return

        if complete and walls == 15:
            self.draw_colored_cell(x, y, self.pattern_color)

        if complete and entry:
            self.draw_colored_cell(x, y, ENTRY_COLOR)

        if complete and exit:
            self.draw_colored_cell(x, y, EXIT_COLOR)

        if walls & 1 == 1:
            self.draw_top_wall(x, y)

        if (walls >> 1) & 1 == 1:
            self.draw_right_wall(x, y)

        if (walls >> 2) & 1 == 1:
            self.draw_bottom_wall(x, y)

        if (walls >> 3) & 1 == 1:
            self.draw_left_wall(x, y)

    def draw_top_wall(self, x: int, y: int) -> None:
        cell_width = self.cell_size[0]

        end_y = y + self.wall_width
        end_x = x + cell_width

        self.pixels[y:end_y, x:end_x] = self.wall_color

    def draw_right_wall(self, x: int, y: int) -> None:
        cell_width, cell_height = self.cell_size

        end_y = y + cell_height
        start_x = x + cell_width - self.wall_width
        end_x = x + cell_width

        self.pixels[y:end_y, start_x:end_x] = self.wall_color

    def draw_bottom_wall(self, x: int, y: int) -> None:
        cell_width, cell_height = self.cell_size

        start_y = y + cell_height - self.wall_width
        end_y = y + cell_height
        end_x = x + cell_width

        self.pixels[start_y:end_y, x:end_x] = self.wall_color

    def draw_left_wall(self, x: int, y: int) -> None:
        cell_height = self.cell_size[1]

        end_y = y + cell_height
        end_x = x + self.wall_width

        self.pixels[y:end_y, x:end_x] = self.wall_color

    def draw_colored_cell(self, x: int, y: int, color: int) -> None:
        cell_width, cell_height = self.cell_size

        padding = self.wall_width

        start_y = y + padding
        start_x = x + padding

        end_y = y + cell_height - padding
        end_x = x + cell_width - padding

        self.pixels[start_y:end_y, start_x:end_x] = color

    def clear_cell(self, cell: tuple[int, int]) -> None:
        cell_width, cell_height = self.cell_size

        x, y = self.cell_coords(cell)

        end_y = y + cell_height
        end_x = x + cell_width

        self.pixels[y:end_y, x:end_x] = 0

    def switch_colors(self) -> None:
        self.wall_color = next(self.wall_colors)

    def get_wall_width(self, cell: tuple[int, int]) -> int:

        min_dimension = min(cell)

        if min_dimension < 20:
            return 1

        if min_dimension < 80:
            return 2

        if min_dimension < 120:
            return 6

        else:
            return 12
