# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  mlx_window.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/09/03 19:41:52 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Any
from time import sleep, time

from .constants import (
    KEY_ESC,
    EVENT_DESTROY,
    FRAMERATE,
    TEXT_COLOR
)


def sync_frame(last_frame_time: float, framerate: int) -> None:
    time_delta = time() - last_frame_time

    time_per_frame = 1 / (framerate if framerate > 0 else 60)

    if time_delta < time_per_frame:
        sleep(time_per_frame - time_delta)


class MlxWindow:
    def __init__(self, name: str) -> None:
        self.mlx = Mlx()
        self.name = name

        self.loop_counter = 0

    def create_window(self, width: int, height: int) -> None:
        self.win_width = width
        self.win_height = height
        self.time = time()

        self.init_mlx()
        self.init_hooks()

    def init_mlx(self) -> None:
        self.mlx_ptr = self.mlx.mlx_init()

        self.mlx_win = self.mlx.mlx_new_window(
            self.mlx_ptr, self.win_width,
            self.win_height, self.name
        )

    def init_hooks(self) -> None:
        self.mlx.mlx_hook(self.mlx_win,
                          EVENT_DESTROY, 0, self.destroy_handler, None)

        self.mlx.mlx_key_hook(self.mlx_win, self.key_handler, None)

        self.mlx.mlx_loop_hook(self.mlx_ptr, self.loop, None)

    def run(self) -> None:
        self.mlx.mlx_loop(self.mlx_ptr)

    def loop(self, _: Any) -> None:
        sync_frame(self.time, FRAMERATE)
        self.time = time()

        self.loop_counter += 1

    def put_image(self, image: Any, x: int, y: int) -> None:

        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr,
            self.mlx_win,
            image, x, y
        )

    def clear_window(self) -> None:
        self.mlx.mlx_clear_window(self.mlx_ptr, self.mlx_win)

    def put_string(self, text: str, x: int, y: int) -> None:

        self.mlx.mlx_string_put(
            self.mlx_ptr,
            self.mlx_win,
            x, y,
            TEXT_COLOR,
            text
        )

    def close(self) -> None:
        self.mlx.mlx_destroy_window(self.mlx_ptr, self.mlx_win)
        self.mlx.mlx_loop_exit(self.mlx_ptr)

    def key_handler(self, keycode: int, _: Any) -> None:
        if keycode == KEY_ESC:
            self.close()

    def destroy_handler(self, _: Any) -> None:
        self.close()
