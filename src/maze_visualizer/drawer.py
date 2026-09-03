# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  drawer.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 12:17:20 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 12:56:29 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from numpy import ndarray


class Drawer:
    def __init__(self, pixels: ndarray, cell_size: int) -> None:
        self.pixels = pixels
        self.cell_size = cell_size

    def cell_coords(self, cell: tuple[int, int]) -> tuple[int, int]:
        col, row = cell

        return (
            col * self.cell_size,
            row * self.cell_size
        )
