# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 18:54:32 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 14:40:23 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from dataclasses import dataclass
from .types import MazeData, Cell, Step


@dataclass
class Maze:
    data: MazeData
    width: int
    height: int
    entry: Cell
    exit: Cell
    solution: list[Cell]
    steps: list[Step]
