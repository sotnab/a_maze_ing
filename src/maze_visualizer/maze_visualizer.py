# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_visualizer.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/08/22 15:51:33 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Final

from src.maze_config import MazeConfig
from src.maze_generator import MazeGen
from .maze_image import MazeImage, CELL_SIZE
from .mlx_window import MlxWindow

KEY_ESC: Final[int] = 65307
EVENT_DESTROY: Final[int] = 33


class MazeVisualizer(MlxWindow):
    def __init__(self, config: MazeConfig) -> None:
        self.generator = MazeGen(config)
        self.maze = self.generator.generate()
        width = self.maze.width * CELL_SIZE
        height = self.maze.height * CELL_SIZE

        super().__init__(width, height, "A Maze Ing")
        self.put_maze()

    def put_maze(self) -> None:
        self.maze_image = MazeImage(
            self.mlx, self.mlx_ptr, self.win_width, self.win_height, self.maze
        )

        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr, self.mlx_win, self.maze_image.image, 0, 0
        )
