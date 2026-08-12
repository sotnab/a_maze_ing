# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_visualizer.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/08/12 23:15:47 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Final, Any
from time import sleep

from src.maze_generator import Maze
from .maze_image import MazeImage, CELL_SIZE

KEY_ESC: Final[int] = 65307
EVENT_CLOSE: Final[int] = 17


class MazeVisualizer:
    def __init__(self, maze: Maze) -> None:
        self.mlx = Mlx()
        self.maze = maze
        self.win_width = maze.width * CELL_SIZE
        self.win_height = maze.height * CELL_SIZE

        self.init_mlx()
        self.maze_image = MazeImage(
            self.mlx, self.mlx_ptr, self.win_width, self.win_height, maze
        )
        self.put_maze()
        self.init_hooks()

    def run(self) -> None:
        self.mlx.mlx_loop(self.mlx_ptr)

    def close(self) -> None:
        self.mlx.mlx_destroy_window(self.mlx_ptr, self.mlx_win)
        self.mlx.mlx_loop_exit(self.mlx_ptr)

    def init_mlx(self) -> None:
        self.mlx_ptr = self.mlx.mlx_init()

        self.mlx_win = self.mlx.mlx_new_window(
            self.mlx_ptr,
            self.win_width,
            self.win_height,
            "A Maze Ing"
        )

    def loop(self, _: Any) -> None:
        sleep(1 / 60)

    def put_maze(self) -> None:
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.mlx_win, self.maze_image.image, 0, 0
        )

    def init_hooks(self) -> None:
        self.mlx.mlx_key_hook(self.mlx_win, self.key_handler, None)
        self.mlx.mlx_hook(self.mlx_win, EVENT_CLOSE, 0, self.close, None)
        self.mlx.mlx_loop_hook(self.mlx_ptr, self.loop, None)

    def key_handler(self, keycode: int, _: Any) -> None:
        if keycode == KEY_ESC:
            self.close()
