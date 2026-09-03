# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_image.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 20:35:12 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 14:32:56 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Any
import numpy

from src.maze_generator import Maze
from .mlx_image import MlxImage
from .wall_drawer import WallDrawer
from .path_drawer import PathDrawer
from .constants import (
    BACKGROUND_COLOR, CELL_SIZE
)


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

        self.init_maze()

    def init_maze(self) -> None:
        buffer = numpy.frombuffer(self.addr, dtype=numpy.uint32)
        buffer.fill(BACKGROUND_COLOR)

        self.pixels = buffer.reshape((self.height, self.width))

        self.wall_drawer = WallDrawer(self.pixels, CELL_SIZE)
        self.path_drawer = PathDrawer(self.pixels, CELL_SIZE)

    def render_step(self, step: tuple[int, int, int]) -> None:
        col, row, walls = step

        self.wall_drawer.clear_cell((col, row))
        self.wall_drawer.draw_walls(walls, (col, row),  False)

    def render_path(self) -> None:
        self.path_drawer.draw_path(self.maze.solution)

    def render_complete(self) -> None:

        for col in range(self.maze.width):
            for row in range(self.maze.height):

                walls = int(self.maze.data[row][col], 16)
                self.wall_drawer.draw_walls(walls, (col, row), True)
