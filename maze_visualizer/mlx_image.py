# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  mlx_image.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 20:48:30 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 21:37:43 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import numpy

from mlx import Mlx
from typing import Any


class MlxImage:
    """Represent a MinilibX image as a NumPy pixel buffer."""

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
        """Initialize the image buffer and metadata."""

        self.mlx = mlx
        self.mlx_ptr = mlx_ptr
        self.width = width
        self.height = height

        self.create_image()

    def create_image(self) -> None:
        """Create the underlying MinilibX image and its buffer."""
        self.image = self.mlx.mlx_new_image(
            self.mlx_ptr, self.width, self.height)

        image_data = self.mlx.mlx_get_data_addr(self.image)
        self.addr = image_data[0]
        self.bytes_per_px = image_data[1]
        self.line_len = image_data[2]

        self.init_pixels()

    def init_pixels(self) -> None:
        """Create the pixel array used for drawing."""

        buffer = numpy.frombuffer(self.addr, dtype=numpy.uint32)
        self.pixels = buffer.reshape((self.height, self.width))
        self.pixels.fill(0)

    def load_bitmap(
                self, filename: str,
                x: int, y: int,
                width: int, height: int
    ) -> None:
        """Load a bitmap sprite into the image surface."""

        with open(filename, "rb") as file:
            data = file.read()

        sprite_buffer = numpy.frombuffer(data[138:], dtype=numpy.uint32)
        sprite_pixels = sprite_buffer.reshape((height, width))
        reversed_pixels = sprite_pixels[::-1, ::]

        end_y = y + height
        end_x = x + width

        self.pixels[y:end_y, x:end_x] = reversed_pixels
