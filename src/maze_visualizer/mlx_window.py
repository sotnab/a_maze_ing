# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  mlx_window.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/08/13 12:32:23 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from mlx import Mlx
from typing import Final, Any
from time import sleep


KEY_ESC: Final[int] = 65307
EVENT_DESTROY: Final[int] = 33


class MlxWindow:
    def __init__(self, width: int, height: int, name: str) -> None:
        self.mlx = Mlx()
        self.win_width = width
        self.win_height = height
        self.name = name

        self.init_mlx()
        self.init_hooks()

    def init_mlx(self) -> None:
        self.mlx_ptr = self.mlx.mlx_init()

        self.mlx_win = self.mlx.mlx_new_window(
            self.mlx_ptr,
            self.win_width,
            self.win_height,
            self.name
        )

    def init_hooks(self) -> None:
        self.mlx.mlx_hook(self.mlx_win,
                          EVENT_DESTROY, 0, self.destroy_handler, None)
        self.mlx.mlx_key_hook(self.mlx_win, self.key_handler, None)
        self.mlx.mlx_loop_hook(self.mlx_ptr, self.loop, None)

    def run(self) -> None:
        self.mlx.mlx_loop(self.mlx_ptr)

    def loop(self, _: Any) -> None:
        sleep(1 / 60)

    def close(self) -> None:
        self.mlx.mlx_destroy_window(self.mlx_ptr, self.mlx_win)
        self.mlx.mlx_loop_exit(self.mlx_ptr)

    def key_handler(self, keycode: int, _: Any) -> None:
        if keycode == KEY_ESC:
            self.close()

    def destroy_handler(self, _: Any) -> None:
        self.close()
