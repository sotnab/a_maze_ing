# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  drawer.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 12:17:20 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 15:11:59 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray

from src.maze_gen import Cell


class Drawer:
    def __init__(self, pixels: ndarray, cell_size: tuple[int, int]) -> None:
        self.pixels = pixels
        self.set_cell_size(cell_size)

    def set_cell_size(self, cell_size: tuple[int, int]) -> None:
        width, height = cell_size

        self.cell_width = width
        self.cell_height = height

    def cell_coords(self, cell: Cell) -> tuple[int, int]:
        x, y = cell

        return (
            x * self.cell_width,
            y * self.cell_height
        )
