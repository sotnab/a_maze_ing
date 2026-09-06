# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_image.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 20:35:12 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 15:39:12 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Any
import numpy

from maze_gen import Maze
from ..mlx_image import MlxImage
from ..drawers.wall_drawer import WallDrawer
from ..drawers.path_drawer import PathDrawer


class MazeImage(MlxImage):
    pixels: numpy.ndarray

    def __init__(
        self, mlx: Mlx,
        mlx_ptr: Any,
        width: int,
        height: int
    ) -> None:

        super().__init__(mlx, mlx_ptr, width, height)

        self.path_visible = False

        self.wall_drawer = WallDrawer(self.pixels, (1, 1))
        self.path_drawer = PathDrawer(self.pixels, (1, 1))

    def set_maze(self, maze: Maze) -> None:
        self.maze = maze

        cell_width = self.width // maze.width
        cell_height = self.height // maze.height

        cell_size = (cell_width, cell_height)

        self.wall_drawer.set_cell_size(cell_size)
        self.path_drawer.set_cell_size(cell_size)

        self.path_visible = False

        self.pixels.fill(0)

    def start_maze_animation(self) -> None:
        self.maze_animation_index = 0

    def start_path_animation(self) -> None:
        self.render_complete()
        self.path_animation_index = 0
        self.last_move = self.maze.entry

    def render_maze_step(self, speed: int) -> bool:

        for _ in range(speed):
            if len(self.maze.steps) == self.maze_animation_index:
                self.render_complete()
                return True

            col, row, walls = self.maze.steps[self.maze_animation_index]

            self.wall_drawer.clear_cell((col, row))
            self.wall_drawer.draw_walls(walls, (col, row),  False)

            self.maze_animation_index += 1

        return False

    def render_path_step(self, speed: int) -> bool:

        for _ in range(max(speed // 5, 1)):
            if len(self.maze.solution) == self.path_animation_index:
                self.render_path()
                return True

            move = self.maze.solution[self.path_animation_index]

            self.path_drawer.connect_cells(self.last_move, move)

            self.last_move = move
            self.path_animation_index += 1

        return False

    def render_complete(self) -> None:

        self.pixels.fill(0)

        for col in range(self.maze.width):
            for row in range(self.maze.height):

                walls = int(self.maze.data[row][col], 16)
                pos = (col, row)

                if pos == self.maze.entry:
                    self.wall_drawer.draw_walls(walls, pos, True, entry=True)
                elif pos == self.maze.exit:
                    self.wall_drawer.draw_walls(walls, pos, True, exit=True)
                else:
                    self.wall_drawer.draw_walls(walls, pos, True)

    def render_path(self) -> None:

        self.path_drawer.draw_path(self.maze.solution)
        self.path_visible = True

    def remove_path(self) -> None:

        self.pixels.fill(0)
        self.render_complete()
        self.path_visible = False

    def switch_colors(self) -> None:

        self.wall_drawer.switch_colors()
        self.render_complete()

        if self.path_visible:
            self.render_path()
