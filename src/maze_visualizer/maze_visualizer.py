# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_visualizer.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 21:41:22 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any

from src.maze_generator import MazeGen
from .maze_image import MazeImage
from .mlx_window import MlxWindow
from .constants import (
    CELL_SIZE, KEY_1, KEY_2, KEY_3, KEY_4
)


class MazeVisualizer(MlxWindow):
    def __init__(self, config_file: str) -> None:
        self.generator = MazeGen(config_file)

        self.maze = self.generator.generate()

        super().__init__("A Maze Ing")

    def display_window(self) -> None:

        width = self.maze.width * CELL_SIZE
        height = (self.maze.height + 1) * CELL_SIZE

        self.create_window(width, height)

        self.maze_image = MazeImage(
            self.mlx,
            self.mlx_ptr,
            self.win_width,
            self.win_height,
            self.maze
        )

        self.maze_image.start_maze_animation()

        self.run()

    def regenerate_maze(self) -> None:

        prev_width = self.maze.width
        prev_height = self.maze.height

        self.maze = self.generator.generate()

        if prev_width != self.maze.width or prev_height != self.maze.height:
            self.close()
            self.display_window()

        self.maze_image.set_maze(self.maze)

        self.maze_image.start_maze_animation()

    def loop(self, _: Any) -> None:

        if self.maze_image.maze_animation:
            self.maze_image.render_gen_step()

        if self.maze_image.path_animation and self.loop_counter % 2 == 0:
            self.maze_image.render_path_step()

        self.put_maze_image()

        super().loop(_)

    def key_handler(self, keycode: int, _: Any) -> None:

        super().key_handler(keycode, _)

        if keycode == KEY_1:
            self.regenerate_maze()

        if keycode == KEY_2:

            if not self.maze_image.maze_animation \
                    and not self.maze_image.path_visible:
                self.maze_image.start_path_animation()

            if self.maze_image.path_visible:
                self.maze_image.clear_path()

        if keycode == KEY_3:

            if self.maze_image.maze_animation:
                self.maze_image.skip_maze_animation()

            if self.maze_image.path_animation:
                self.maze_image.skip_path_animation()

        if keycode == KEY_4:
            self.maze_image.switch_colors()

    def put_maze_image(self) -> None:

        self.put_image(self.maze_image.image, 0, 0)

        str_pos_y = self.win_height - CELL_SIZE + (CELL_SIZE // 4)

        self.put_string("Regenerate: 1", 10, str_pos_y)
        self.put_string("Show path: 2", 170, str_pos_y)
        self.put_string("Skip: 3", 310, str_pos_y)
        self.put_string("Switch colors: 4", 400, str_pos_y)
