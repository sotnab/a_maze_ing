# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  wall_drawer.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/14 00:39:51 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 13:02:00 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray
from typing import Final

from .drawer import Drawer

PLATINIUM: Final[int] = 0xFF778DA9
LIGHT_BLUE: Final[int] = 0xFF415A77
BLUE: Final[int] = 0xFF1B263B
WALL_WIDTH: Final[int] = 2


class WallDrawer(Drawer):
    def __init__(self, pixels: ndarray, cell_size: int) -> None:
        super().__init__(pixels, cell_size)

        self.wall_width = WALL_WIDTH

    def draw_walls(
            self, walls: int, cell: tuple[int, int], finish: bool) -> None:

        x, y = self.cell_coords(cell)

        if not finish and walls == 15:
            return

        if finish and walls == 15:
            return self.draw_closed_cell(x, y)

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

        self.pixels[y:end_y, x:end_x] = LIGHT_BLUE

    def draw_right_wall(self, x: int, y: int) -> None:
        end_y = y + self.cell_size
        start_x = x + self.cell_size - self.wall_width
        end_x = x + self.cell_size

        self.pixels[y:end_y, start_x:end_x] = LIGHT_BLUE

    def draw_bottom_wall(self, x: int, y: int) -> None:
        start_y = y + self.cell_size - self.wall_width
        end_y = y + self.cell_size
        end_x = x + self.cell_size

        self.pixels[start_y:end_y, x:end_x] = LIGHT_BLUE

    def draw_left_wall(self, x: int, y: int) -> None:
        end_y = y + self.cell_size
        end_x = x + self.wall_width

        self.pixels[y:end_y, x:end_x] = LIGHT_BLUE

    def draw_closed_cell(self, x: int, y: int) -> None:
        end_y = y + self.cell_size
        end_x = x + self.cell_size

        self.pixels[y:end_y, x:end_x] = PLATINIUM

    def clear_cell(self, cell: tuple[int, int]) -> None:
        x, y = self.cell_coords(cell)

        end_y = y + self.cell_size
        end_x = x + self.cell_size

        self.pixels[y:end_y, x:end_x] = BLUE
