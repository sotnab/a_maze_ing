# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 18:54:32 by wbaran          #+#    #+#               #
#  Updated: 2026/08/12 18:57:36 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from dataclasses import dataclass


@dataclass
class Maze:
    data: str
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
