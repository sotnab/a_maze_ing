# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 18:54:32 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 21:37:43 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from dataclasses import dataclass
from .types import MazeData, Cell, Step


@dataclass
class Maze:
    """Store generated maze data, the path, and animation steps."""

    data: MazeData
    width: int
    height: int
    entry: Cell
    exit: Cell
    solution: list[Cell]
    steps: list[Step]
