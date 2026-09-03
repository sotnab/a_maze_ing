# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  constants.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 14:21:39 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 20:49:00 by wbaran          ###   ########.fr        #
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
PATH_COLOR: Final[int] = 0xFF286655
TEXT_COLOR: Final[int] = 0xFFe1e5f2

# Wall colors
COLORS: Final[tuple[int, ...]] = (
    0xFF445c87,
    0xFFc3c7d4,
    0xFFffb703,
    0xFFe76f51,
    0xFF000000,
    0xFFadc178
)
# Keycodes
KEY_ESC: Final[int] = 65307
KEY_1: Final[int] = 49
KEY_2: Final[int] = 50
KEY_3: Final[int] = 51
KEY_4: Final[int] = 52
KEY_5: Final[int] = 53

# Xwindow server events
EVENT_DESTROY: Final[int] = 33
