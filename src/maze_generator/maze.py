# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 18:54:32 by wbaran          #+#    #+#               #
#  Updated: 2026/08/22 15:42:05 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from dataclasses import dataclass


@dataclass
class Maze:
    data: list[str]
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    solution: list[tuple[int, int]]
