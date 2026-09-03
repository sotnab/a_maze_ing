# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  constants.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 14:17:32 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 14:36:23 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


PATTERN_42 = (
    "X.X.XXX",
    "X.X...X",
    "XXX.XXX",
    "..X.X..",
    "..X.XXX",
)

NORTH = 0b0001
EAST = 0b0010
SOUTH = 0b0100
WEST = 0b1000

ALL_WALLS = 0b1111

REMOVE_NORTH = 0b1110
REMOVE_EAST = 0b1101
REMOVE_SOUTH = 0b1011
REMOVE_WEST = 0b0111
