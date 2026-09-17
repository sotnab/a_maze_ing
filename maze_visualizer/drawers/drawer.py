# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  drawer.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 12:17:20 by wbaran          #+#    #+#               #
#  Updated: 2026/09/17 17:42:45 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray

from mazegen import Cell


class Drawer:
    """Store pixel data and cell sizing for drawing helpers."""

    def __init__(self, pixels: ndarray, cell_size: tuple[int, int]) -> None:
        """Initialize the drawer with pixel data and a cell size."""

        width, height = cell_size

        self.pixels = pixels
        self.cell_width = width
        self.cell_height = height

    def cell_coords(self, cell: Cell) -> tuple[int, int]:
        """Return the pixel coordinates of a cell."""
        x, y = cell

        return (
            x * self.cell_width,
            y * self.cell_height
        )
