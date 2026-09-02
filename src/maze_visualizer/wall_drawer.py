# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  wall_drawer.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/14 00:39:51 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 00:14:56 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import numpy
from typing import Final


PLATINIUM: Final[int] = 0xFF778DA9
LIGHT_BLUE: Final[int] = 0xFF415A77
BLUE: Final[int] = 0xFF1B263B


class WallDrawer:
    def __init__(
                self,
                pixels: numpy.ndarray,
                cell_size: int,
                wall_width: int
            ) -> None:
        self.pixels = pixels
        self.cell_size = cell_size
        self.wall_width = wall_width

    def draw_walls(self, walls: int, row: int, col: int, finish: bool) -> None:
        cell_x = self.cell_size * col
        cell_y = self.cell_size * row

        if not finish and walls == 15:
            return

        if finish and walls == 15:
            return self.draw_closed_cell(cell_x, cell_y)

        if walls & 1 == 1:
            self.draw_top_wall(cell_x, cell_y)

        if (walls >> 1) & 1 == 1:
            self.draw_right_wall(cell_x, cell_y)

        if (walls >> 2) & 1 == 1:
            self.draw_bottom_wall(cell_x, cell_y)

        if (walls >> 3) & 1 == 1:
            self.draw_left_wall(cell_x, cell_y)

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

    def clear_cell(self, row: int, col: int) -> None:
        x = self.cell_size * col
        y = self.cell_size * row

        end_x = x + self.cell_size
        end_y = y + self.cell_size

        self.pixels[x:end_x, y:end_y] = BLUE
