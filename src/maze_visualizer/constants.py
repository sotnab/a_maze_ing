# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  constants.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 14:21:39 by wbaran          #+#    #+#               #
#  Updated: 2026/09/04 01:22:02 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Final

# Max framerate
FRAMERATE: Final[int] = 60

# Sizes
WALL_WIDTH: Final[int] = 2
WINDOW_WIDTH: Final[int] = 1200
WINDOW_HEIGHT: Final[int] = 800
INSTRUCTIONS_HEIGHT: Final[int] = 30

# Colors
BACKGROUND_COLOR: Final[int] = 0xFF222b36
TEXT_COLOR: Final[int] = 0xFFe1e5f2

PATH_COLOR: Final[int] = 0xFF286655
ENTRY_COLOR: Final[int] = 0x10588157
EXIT_COLOR: Final[int] = 0x109b2226
PATTERN_COLOR: Final[int] = 0x10c3c7d4

# Offsets for instructions
REGENERATE_OFFSET: Final[int] = 200
SHOW_PATH_OFFSET: Final[int] = 390
SKIP_OFFSET: Final[int] = 570
SWITCH_COLORS_OFFSET: Final[int] = 800

# Wall colors
WALL_COLORS: Final[tuple[int, ...]] = (
    0xFF445c87,
    0xFF000000,
    0xFF9d4edd,
    0xFF4f772d,
    0xFFc97c5d,
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
