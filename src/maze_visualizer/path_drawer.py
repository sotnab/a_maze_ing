# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  path_drawer.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 10:37:47 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 13:04:45 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray
from typing import Final

from .drawer import Drawer

DARK_BLUE: Final[int] = 0x88386641


class PathDrawer(Drawer):
    def __init__(self, pixels: ndarray, cell_size: int) -> None:
        super().__init__(pixels, cell_size)

        self.path_width = self.cell_size // 5

    def connect_down(self, cell: tuple[int, int]) -> None:
        x, y = self.cell_coords(cell)

        offset = (self.cell_size // 2) - (self.path_width // 2)

        start_y = y + offset
        start_x = x + offset

        end_y = start_y + self.path_width + self.cell_size
        end_x = start_x + self.path_width

        self.pixels[start_y:end_y, start_x:end_x] = DARK_BLUE

    def connect_right(self, cell: tuple[int, int]) -> None:
        x, y = self.cell_coords(cell)

        offset = (self.cell_size // 2) - (self.path_width // 2)

        start_y = y + offset
        start_x = x + offset

        end_y = start_y + self.path_width
        end_x = start_x + self.path_width + self.cell_size

        self.pixels[start_y:end_y, start_x:end_x] = DARK_BLUE

    def connect_cells(
            self, cell1: tuple[int, int], cell2: tuple[int, int]) -> None:
        col1, row1 = cell1
        col2, row2 = cell2

        if col1 == col2 and row1 < row2:
            self.connect_down(cell1)

        if col1 == col2 and row1 > row2:
            self.connect_down(cell2)

        if col1 < col2 and row1 == row2:
            self.connect_right(cell1)

        if col1 > col2 and row1 == row2:
            self.connect_right(cell2)

    def draw_path(self, path: list[tuple[int, int]]) -> None:

        for index, cell in enumerate(path):
            if index > 0:
                self.connect_cells(cell, path[index - 1])
