# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_visualizer.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/09/02 21:55:54 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Final

from src.maze_generator import MazeGen
from .maze_image import MazeImage, CELL_SIZE
from .mlx_window import MlxWindow

KEY_ESC: Final[int] = 65307
KEY_R: Final[int] = 114
EVENT_DESTROY: Final[int] = 33


class MazeVisualizer(MlxWindow):
    def __init__(self, config_file: str) -> None:
        super().__init__("A Maze Ing")

        self.generator = MazeGen(config_file)

    def generate_maze(self) -> None:
        self.maze = self.generator.generate()

        width = self.maze.width * CELL_SIZE
        height = self.maze.height * CELL_SIZE

        self.create_window(width, height)
        self.create_maze_image()
        self.run()

    def loop(self, _: Any) -> None:
        self.put_maze_image()

        super().loop(_)

    def key_handler(self, keycode: int, _: Any) -> None:
        super().key_handler(keycode, _)
        if keycode == KEY_R:
            self.close()
            self.generate_maze()

    def create_maze_image(self) -> None:
        self.maze_image = MazeImage(
            self.mlx,
            self.mlx_ptr,
            self.win_width,
            self.win_height,
            self.maze
        )

    def put_maze_image(self) -> None:
        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr,
            self.mlx_win,
            self.maze_image.image,
            0, 0
        )
