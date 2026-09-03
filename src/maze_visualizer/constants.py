# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  constants.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 14:21:39 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 19:22:22 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Final

# Max framerate
FRAMERATE: Final[int] = 60

# Sizes
CELL_SIZE: Final[int] = 40
WALL_WIDTH: Final[int] = 2

# Colors
BACKGROUND_COLOR: Final[int] = 0xFF222b36
WALL_COLOR: Final[int] = 0xFF445c87
PATTERN_COLOR: Final[int] = 0xFFc3c7d4
PATH_COLOR: Final[int] = 0xFF286655
TEXT_COLOR: Final[int] = 0xFFFFFFFF

# Keycodes
KEY_ESC: Final[int] = 65307
KEY_R: Final[int] = 114
KEY_P: Final[int] = 112
KEY_S: Final[int] = 115

# Xwindow server events
EVENT_DESTROY: Final[int] = 33
