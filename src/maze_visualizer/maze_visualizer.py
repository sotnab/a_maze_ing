# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_visualizer.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 19:21:51 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from sys import stderr
from typing import Any
from math import sqrt, floor
from pydantic import ValidationError

from src.maze_generator import MazeGen, MazeConfig, MazeAlgorithm
from .background_image import BackgroundImage
from .title_image import TitleImage
from .maze_image import MazeImage
from .mlx_window import MlxWindow
from .constants import (
    KEY_1, KEY_2, KEY_3,
    KEY_4, KEY_5, KEY_6, KEY_7,
    MAZE_WIDTH, MAZE_HEIGHT,
    WINDOW_HEIGHT, WINDOW_WIDTH,
    TITLE_SPRITE_HEIGHT,
    TITLE_SPRITE_WIDTH
)


class MazeVisualizer(MlxWindow):
    def __init__(self, config_file: str) -> None:

        super().__init__("A Maze Ing")

        self.maze_visible = False

        self.generator = MazeGen(config_file)

        self.background_image = BackgroundImage(
            self.mlx,
            self.mlx_ptr,
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

        self.title_image = TitleImage(
            self.mlx,
            self.mlx_ptr,
            TITLE_SPRITE_WIDTH,
            TITLE_SPRITE_HEIGHT
        )

        self.maze_image = MazeImage(
            self.mlx,
            self.mlx_ptr,
            MAZE_WIDTH,
            MAZE_HEIGHT
        )

    def show_window(self) -> None:

        self.create_window(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.put_background()
        self.put_title()

        self.run()

    def show_maze(self, algorithm: MazeAlgorithm) -> None:
        maze = self.generator.generate(algorithm)

        area = maze.width * maze.height
        root = floor(sqrt(area)) // 10

        self.animation_speed = max((root, 1))

        self.maze_image.set_maze(maze)
        self.maze_image.start_maze_animation()

        self.maze_visible = True

    def loop(self, _: Any) -> None:

        if self.maze_visible:

            if self.maze_image.maze_animation:
                self.maze_image.render_gen_step(self.animation_speed)

            if self.maze_image.path_animation:
                self.maze_image.render_path_step(self.animation_speed)

        self.put_background()

        if not self.maze_visible:
            self.put_title()
        else:
            self.put_maze()

        super().loop(_)

    def key_handler(self, keycode: int, _: Any) -> None:

        super().key_handler(keycode, _)

        try:
            if keycode == KEY_1:
                self.show_maze(MazeAlgorithm.DFS)

            if keycode == KEY_2:
                self.show_maze(MazeAlgorithm.WILSON)

            if keycode == KEY_3:
                self.show_maze(MazeAlgorithm.PRIMS)

        except (ValidationError) as e:
            MazeConfig.handle_validation_error(e)

        except (ValueError, PermissionError, UnicodeDecodeError) as e:
            print(e, file=stderr)

        if keycode == KEY_4:
            self.maze_image.start_path_animation()

        if keycode == KEY_5:
            self.maze_image.skip_animation()

        if keycode == KEY_6:
            self.maze_visible = False

        if keycode == KEY_7:
            self.maze_image.switch_colors()

    def put_maze(self) -> None:
        self.put_image(self.maze_image.image, 0, 0)

    def put_background(self) -> None:
        self.put_image(self.background_image.image, 0, 0)

    def put_title(self) -> None:

        pos_x = (MAZE_WIDTH // 2) - (TITLE_SPRITE_WIDTH // 2)
        pos_y = (MAZE_HEIGHT // 2) - (TITLE_SPRITE_HEIGHT // 2)

        self.put_image(self.title_image.image, pos_x, pos_y)
