# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  image.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 20:48:30 by wbaran          #+#    #+#               #
#  Updated: 2026/08/12 22:32:41 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Any


class Image:
    image: Any
    addr: memoryview
    bytes_per_px: int
    line_len: int

    def __init__(
        self,
        mlx: Mlx,
        mlx_ptr: Any,
        width: int,
        height: int
    ) -> None:
        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.width = width
        self.height = height
        self.create_image()

    def create_image(self) -> None:
        self.image = self.mlx.mlx_new_image(
            self.mlx_ptr, self.width, self.height)

        image_data = self.mlx.mlx_get_data_addr(self.image)
        self.addr = image_data[0]
        self.bytes_per_px = image_data[1]
        self.line_len = image_data[2]
