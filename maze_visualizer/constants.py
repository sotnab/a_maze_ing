# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  constants.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/03 14:21:39 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 15:35:49 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Final

# Max framerate
FRAMERATE: Final[int] = 60

# Sizes
WALL_WIDTH: Final[int] = 2

MAZE_WIDTH: Final[int] = 1200
MAZE_HEIGHT: Final[int] = 860

WINDOW_TITLE: Final[str] = "A Maze Ing"

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

# Colors
BACKGROUND_COLOR: Final[int] = 0xFF222b36
TEXT_COLOR: Final[int] = 0xFFe1e5f2

PATH_COLOR: Final[int] = 0xFF286655
ENTRY_COLOR: Final[int] = 0xcc588157
EXIT_COLOR: Final[int] = 0xcc9b2226
PATTERN_COLOR: Final[int] = 0xccc3c7d4

# Wall colors
WALL_COLORS: Final[tuple[int, ...]] = (
    0xFF445c87,
    0xFF52796F,
    0xFF8E7D5B,
    0xFF8C6B73,
    0xFF5B7B88,
    0xFF9E6B60,
    0xFF756980
)
# Keycodes
KEY_ESC: Final[int] = 65307
KEY_1: Final[int] = 49
KEY_2: Final[int] = 50
KEY_3: Final[int] = 51
KEY_4: Final[int] = 52
KEY_5: Final[int] = 53
KEY_6: Final[int] = 54
KEY_7: Final[int] = 55

# Xwindow server events
EVENT_DESTROY: Final[int] = 33

# Sprites

BG_SPRITE: Final[str] = \
    "./maze_visualizer/sprites/background.bmp"

BG_SPRITE_WIDTH: Final[int] = 1200
BG_SPRITE_HEIGHT: Final[int] = 900

TITLE_SPRITE: Final[str] = \
    "./maze_visualizer/sprites/title.bmp"

TITLE_SPRITE_WIDTH: Final[int] = 786
TITLE_SPRITE_HEIGHT: Final[int] = 218
