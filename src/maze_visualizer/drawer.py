# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  drawer.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 12:17:20 by wbaran          #+#    #+#               #
#  Updated: 2026/09/04 00:44:54 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray


class Drawer:
    def __init__(self, pixels: ndarray, cell_size: tuple[int, int]) -> None:
        self.pixels = pixels
        self.cell_size = cell_size

    def cell_coords(self, cell: tuple[int, int]) -> tuple[int, int]:
        col, row = cell

        cell_width, cell_height = self.cell_size

        return (
            col * cell_width,
            row * cell_height
        )
