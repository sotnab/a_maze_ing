# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  wall_drawer.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/14 00:39:51 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 21:39:37 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray
from itertools import cycle

from .drawer import Drawer
from .constants import (
    BACKGROUND_COLOR,
    WALL_WIDTH,
    WALL_COLORS,
    PATTERN_COLOR,
    ENTRY_COLOR,
    EXIT_COLOR
)


class WallDrawer(Drawer):
    def __init__(self, pixels: ndarray, cell_size: int) -> None:
        super().__init__(pixels, cell_size)

        self.wall_width = WALL_WIDTH

        self.wall_colors = cycle(WALL_COLORS)

        self.wall_color = next(self.wall_colors)
        self.pattern_color = PATTERN_COLOR

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
        end_y = y + self.wall_width
        end_x = x + self.cell_size

        self.pixels[y:end_y, x:end_x] = self.wall_color

    def draw_right_wall(self, x: int, y: int) -> None:
        end_y = y + self.cell_size
        start_x = x + self.cell_size - self.wall_width
        end_x = x + self.cell_size

        self.pixels[y:end_y, start_x:end_x] = self.wall_color

    def draw_bottom_wall(self, x: int, y: int) -> None:
        start_y = y + self.cell_size - self.wall_width
        end_y = y + self.cell_size
        end_x = x + self.cell_size

        self.pixels[start_y:end_y, x:end_x] = self.wall_color

    def draw_left_wall(self, x: int, y: int) -> None:
        end_y = y + self.cell_size
        end_x = x + self.wall_width

        self.pixels[y:end_y, x:end_x] = self.wall_color

    def draw_colored_cell(self, x: int, y: int, color: int) -> None:
        padding = self.wall_width

        start_y = y + padding
        start_x = x + padding

        end_y = y + self.cell_size - padding
        end_x = x + self.cell_size - padding

        self.pixels[start_y:end_y, start_x:end_x] = color

    def clear_cell(self, cell: tuple[int, int]) -> None:
        x, y = self.cell_coords(cell)

        end_y = y + self.cell_size
        end_x = x + self.cell_size

        self.pixels[y:end_y, x:end_x] = BACKGROUND_COLOR

    def switch_colors(self) -> None:
        self.wall_color = next(self.wall_colors)
