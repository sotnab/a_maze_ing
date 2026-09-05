# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_image.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 20:35:12 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 17:38:33 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Any
import numpy

from src.maze_generator import Maze
from .mlx_image import MlxImage
from .wall_drawer import WallDrawer
from .path_drawer import PathDrawer


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
        self.maze_animation = False
        self.path_animation = False

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
        self.maze_animation = False
        self.path_animation = False

        self.pixels.fill(0)

    def start_maze_animation(self) -> None:

        if hasattr(self, "maze"):
            self.maze_animation_index = 0
            self.maze_animation = True

    def start_path_animation(self) -> None:

        if not self.maze_animation and hasattr(self, "maze"):
            self.render_complete()
            self.path_animation_index = 0
            self.path_animation = True
            self.last_move = self.maze.entry

    def skip_animation(self) -> None:

        if self.maze_animation:
            self.maze_animation = False
            self.render_complete()

        if self.path_animation:
            self.path_animation = False
            self.render_path()

    def render_gen_step(self) -> None:
        if not self.maze_animation:
            return

        if len(self.maze.steps) == self.maze_animation_index:
            self.maze_animation = False
            self.render_complete()
            return

        col, row, walls = self.maze.steps[-1 - self.maze_animation_index]

        self.wall_drawer.clear_cell((col, row))
        self.wall_drawer.draw_walls(walls, (col, row),  False)

        self.maze_animation_index += 1

    def render_path_step(self) -> None:
        if not self.path_animation:
            return

        if len(self.maze.solution) == self.path_animation_index:
            self.path_animation = False
            self.path_visible = True
            self.render_path()
            return

        move = self.maze.solution[self.path_animation_index]

        self.path_drawer.connect_cells(self.last_move, move)

        self.last_move = move
        self.path_animation_index += 1

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

        if hasattr(self, "maze"):
            self.path_drawer.draw_path(self.maze.solution)
            self.path_visible = True

    def switch_colors(self) -> None:

        if not self.maze_animation and not self.path_animation:
            self.wall_drawer.switch_colors()
            self.render_complete()

            if self.path_visible:
                self.render_path()
