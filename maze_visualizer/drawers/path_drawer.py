# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  path_drawer.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 10:37:47 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 16:31:49 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray

from .drawer import Drawer
from ..constants import PATH_COLOR

from maze_gen import Cell


class PathDrawer(Drawer):
    def __init__(self, pixels: ndarray, cell_size: tuple[int, int]) -> None:
        super().__init__(pixels, cell_size)

        self.set_cell_size(cell_size)

    def set_cell_size(self, cell_size: tuple[int, int]) -> None:

        super().set_cell_size(cell_size)
        self.path_width = min((self.cell_width, self.cell_height)) // 5

    def connect_down(self, cell: Cell) -> None:
        x, y = self.cell_coords(cell)

        offset_y = (self.cell_height // 2) - (self.path_width // 2)
        offset_x = (self.cell_width // 2) - (self.path_width // 2)

        start_y = y + offset_y
        start_x = x + offset_x

        end_y = start_y + self.path_width + self.cell_height
        end_x = start_x + self.path_width

        self.pixels[start_y:end_y, start_x:end_x] = PATH_COLOR

    def connect_right(self, cell: Cell) -> None:
        x, y = self.cell_coords(cell)

        offset_y = (self.cell_height // 2) - (self.path_width // 2)
        offset_x = (self.cell_width // 2) - (self.path_width // 2)

        start_y = y + offset_y
        start_x = x + offset_x

        end_y = start_y + self.path_width
        end_x = start_x + self.path_width + self.cell_width

        self.pixels[start_y:end_y, start_x:end_x] = PATH_COLOR

    def connect_cells(self, cell1: Cell, cell2: Cell) -> None:

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

    def draw_path(self, path: list[Cell]) -> None:

        for index, cell in enumerate(path):
            if index > 0:
                self.connect_cells(cell, path[index - 1])
