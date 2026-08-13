# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_image.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 20:35:12 by wbaran          #+#    #+#               #
#  Updated: 2026/08/13 12:51:50 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Any, Final
import numpy

from src.maze_generator import Maze
from .mlx_image import MlxImage


PLATINIUM: Final[int] = 0xFF778DA9
DARK_BLUE: Final[int] = 0xFF0D1B2A
BLUE: Final[int] = 0xFF1B263B
LIGHT_BLUE: Final[int] = 0xFF415A77

CELL_SIZE: Final[int] = 40
WALL_WIDTH: Final[int] = 2


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
        maze_map = self.maze.data.split("\n")

        for row in range(self.maze.height):
            for col in range(self.maze.width):
                walls = int(maze_map[row][col], 16)
                self.draw_walls(walls, row, col)

    def draw_walls(self, walls: int, row: int, col: int) -> None:
        cell_x = CELL_SIZE * col
        cell_y = CELL_SIZE * row

        if walls == 15:
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
        end_y = y + WALL_WIDTH
        end_x = x + CELL_SIZE

        self.pixels[y:end_y, x:end_x] = LIGHT_BLUE

    def draw_right_wall(self, x: int, y: int) -> None:
        end_y = y + CELL_SIZE
        start_x = x + CELL_SIZE - WALL_WIDTH
        end_x = x + CELL_SIZE

        self.pixels[y:end_y, start_x:end_x] = LIGHT_BLUE

    def draw_bottom_wall(self, x: int, y: int) -> None:
        start_y = y + CELL_SIZE - WALL_WIDTH
        end_y = y + CELL_SIZE
        end_x = x + CELL_SIZE

        self.pixels[start_y:end_y, x:end_x] = LIGHT_BLUE

    def draw_left_wall(self, x: int, y: int) -> None:
        end_y = y + CELL_SIZE
        end_x = x + WALL_WIDTH

        self.pixels[y:end_y, x:end_x] = LIGHT_BLUE

    def draw_closed_cell(self, x: int, y: int) -> None:
        end_y = y + CELL_SIZE
        end_x = x + CELL_SIZE

        self.pixels[y:end_y, x:end_x] = PLATINIUM
