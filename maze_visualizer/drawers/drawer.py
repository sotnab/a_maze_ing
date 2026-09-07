# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  drawer.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 12:17:20 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 21:37:43 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray

from maze_gen import Cell


class Drawer:
    """Store pixel data and cell sizing for drawing helpers."""

    def __init__(self, pixels: ndarray, cell_size: tuple[int, int]) -> None:
        """Initialize the drawer with pixel data and a cell size."""
        self.pixels = pixels
        self.set_cell_size(cell_size)

    def set_cell_size(self, cell_size: tuple[int, int]) -> None:
        """Set the size used for each maze cell."""
        width, height = cell_size

        self.cell_width = width
        self.cell_height = height

    def cell_coords(self, cell: Cell) -> tuple[int, int]:
        """Return the pixel coordinates of a cell."""
        x, y = cell

        return (
            x * self.cell_width,
            y * self.cell_height
        )
