# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_gen.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/22 15:14:13 by wbaran          #+#    #+#               #
#  Updated: 2026/08/22 17:14:04 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .maze import Maze
from src.maze_config import MazeConfig


class MazeGen:
    def __init__(self, config: MazeConfig):
        data = ["0" * config.width] * config.height
        self.maze = Maze(data, config.width, config.height,
                         config.entry, config.exit)

    def generate(self) -> Maze:
        return self.maze
