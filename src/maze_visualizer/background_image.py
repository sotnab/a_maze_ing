# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  background_image.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/05 01:41:46 by wbaran          #+#    #+#               #
#  Updated: 2026/09/05 19:06:42 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from mlx import Mlx
from .mlx_image import MlxImage

from .constants import (
    BG_SPRITE, BG_SPRITE_HEIGHT, BG_SPRITE_WIDTH
)


class BackgroundImage(MlxImage):
    def __init__(
            self, mlx: Mlx,
            mlx_ptr: Any,
            width: int,
            height: int
    ) -> None:

        super().__init__(mlx, mlx_ptr, width, height)

        self.load_bitmap(
            BG_SPRITE,
            0, 0,
            BG_SPRITE_WIDTH,
            BG_SPRITE_HEIGHT
        )
