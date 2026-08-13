# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 18:54:32 by wbaran          #+#    #+#               #
#  Updated: 2026/08/14 00:12:51 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from dataclasses import dataclass
import numpy


@dataclass
class Maze:
    data: numpy.ndarray
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
