# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  title_image.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/05 10:03:03 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 19:05:59 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from mlx import Mlx
from .mlx_image import MlxImage

from .constants import (
    TITLE_SPRITE,
    TITLE_SPRITE_HEIGHT,
    TITLE_SPRITE_WIDTH
)


class TitleImage(MlxImage):
    def __init__(
            self, mlx: Mlx,
            mlx_ptr: Any,
            width: int,
            height: int
    ) -> None:

        super().__init__(mlx, mlx_ptr, width, height)

        self.load_bitmap(
            TITLE_SPRITE,
            0, 0,
            TITLE_SPRITE_WIDTH,
            TITLE_SPRITE_HEIGHT
        )
