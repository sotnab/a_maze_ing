# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_image.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 20:35:12 by wbaran          #+#    #+#               #
#  Updated: 2026/08/14 00:49:17 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Any, Final
import numpy

from src.maze_generator import Maze
from .mlx_image import MlxImage
from .wall_drawer import WallDrawer


DARK_BLUE: Final[int] = 0xFF0D1B2A
BLUE: Final[int] = 0xFF1B263B
GREEN: Final[int] = 0xFF386641

CELL_SIZE: Final[int] = 40
WALL_WIDTH: Final[int] = 2
ENTRY_PADDING: Final[int] = 12


class MazeImage(MlxImage):
    pixels: numpy.ndarray

    def __init__(
        self,
        mlx: Mlx,
        mlx_ptr: Any,
        width: int,
        height: int,
        maze: Maze
    ) -> None:
        super().__init__(mlx, mlx_ptr, width, height)
        self.maze = maze
        self.render_maze()

    def render_maze(self) -> None:
        buffer = numpy.frombuffer(self.addr, dtype=numpy.uint32)
        buffer.fill(BLUE)
        self.pixels = buffer.reshape((self.height, self.width))

        self.set_pixels()

    def set_pixels(self) -> None:
        wall_drawer = WallDrawer(self.pixels, CELL_SIZE, WALL_WIDTH)

        for row in range(self.maze.height):
            for col in range(self.maze.width):

                walls = int(self.maze.data[row][col], 16)
                wall_drawer.draw_walls(walls, row, col)
