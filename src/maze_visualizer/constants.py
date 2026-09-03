# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  constants.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 14:21:39 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 14:31:53 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Final

# Max framerate
FRAMERATE: Final[int] = 60

# Sizes
CELL_SIZE: Final[int] = 40
WALL_WIDTH: Final[int] = 2

# Colors
PATTERN_COLOR: Final[int] = 0xFF778DA9
WALL_COLOR: Final[int] = 0xFF415A77
BACKGROUND_COLOR: Final[int] = 0xFF1B263B
PATH_COLOR: Final[int] = 0x88386641

# Keycodes
KEY_ESC: Final[int] = 65307
KEY_R: Final[int] = 114
KEY_P: Final[int] = 112
KEY_S: Final[int] = 115

# Xwindow server events
EVENT_DESTROY: Final[int] = 33
