# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_visualizer.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 12:36:35 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Final

from src.maze_generator import MazeGen
from .maze_image import MazeImage, CELL_SIZE
from .mlx_window import MlxWindow

KEY_ESC: Final[int] = 65307
KEY_R: Final[int] = 114
KEY_P: Final[int] = 112
KEY_S: Final[int] = 115
EVENT_DESTROY: Final[int] = 33


class MazeVisualizer(MlxWindow):
    def __init__(self, config_file: str) -> None:
        self.generator = MazeGen(config_file)
        self.finished_animation = False
        self.skip_animation = False

        super().__init__("A Maze Ing")

    def generate_maze(self) -> None:

        self.maze = self.generator.generate()

        width = self.maze.width * CELL_SIZE
        height = self.maze.height * CELL_SIZE

        self.finished_animation = False
        self.skip_animation = False

        self.create_window(width, height)

        self.maze_image = MazeImage(
            self.mlx,
            self.mlx_ptr,
            self.win_width,
            self.win_height,
            self.maze
        )

        self.run()

    def loop(self, _: Any) -> None:

        if not self.finished_animation:

            if len(self.maze.steps) > 0 and not self.skip_animation:
                step = self.maze.steps.pop()

                self.maze_image.render_step(step)
            else:
                self.maze_image.render_complete()

                self.finished_animation = True

            self.put_maze_image()

        super().loop(_)

    def key_handler(self, keycode: int, _: Any) -> None:
        super().key_handler(keycode, _)

        if keycode == KEY_R:
            self.close()
            self.generate_maze()

        if keycode == KEY_P and self.finished_animation:
            self.maze_image.render_path()
            self.put_maze_image()

        if keycode == KEY_S:
            self.skip_animation = True

    def put_maze_image(self) -> None:
        self.put_image(self.maze_image.image, 0, 0)
