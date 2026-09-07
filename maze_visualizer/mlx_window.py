# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  mlx_window.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 17:38:02 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 21:37:43 by wbaran          ###   ########.fr        #
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
    """Limit the frame rate for smooth animation."""
    time_delta = time() - last_frame_time

    time_per_frame = 1 / (framerate if framerate > 0 else 60)

    if time_delta < time_per_frame:
        sleep(time_per_frame - time_delta)


class MlxWindow:
    """Wrap MinilibX window creation and event handling."""

    def __init__(self, name: str) -> None:
        self.mlx = Mlx()
        self.mlx_ptr = self.mlx.mlx_init()
        self.name = name

        self.loop_counter = 0

    def create_window(self, width: int, height: int) -> None:
        """Create the window and initialize the hooks."""
        self.win_width = width
        self.win_height = height
        self.time = time()

        self.init_window()
        self.init_hooks()

    def init_window(self) -> None:
        """Create the MinilibX window instance."""
        self.mlx_win = self.mlx.mlx_new_window(
            self.mlx_ptr, self.win_width,
            self.win_height, self.name
        )

    def init_hooks(self) -> None:
        """Register the destroy, key, and loop hooks."""
        self.mlx.mlx_hook(self.mlx_win,
                          EVENT_DESTROY, 0, self.destroy_handler, None)

        self.mlx.mlx_key_hook(self.mlx_win, self.key_handler, None)

        self.mlx.mlx_loop_hook(self.mlx_ptr, self.loop, None)

    def run(self) -> None:
        """Start the MinilibX event loop."""
        self.mlx.mlx_loop(self.mlx_ptr)

    def loop(self, _: Any) -> None:
        """Run one frame update step."""
        sync_frame(self.time, FRAMERATE)
        self.time = time()

        self.loop_counter += 1

    def put_image(self, image: Any, x: int, y: int) -> None:
        """Draw an image at the specified position."""

        self.mlx.mlx_put_image_to_window(
            self.mlx_ptr,
            self.mlx_win,
            image, x, y
        )

    def clear_window(self) -> None:
        """Clear the current window content."""
        self.mlx.mlx_clear_window(self.mlx_ptr, self.mlx_win)

    def put_string(self, text: str, x: int, y: int) -> None:
        """Draw text on the current window."""

        self.mlx.mlx_string_put(
            self.mlx_ptr,
            self.mlx_win,
            x, y,
            TEXT_COLOR,
            text
        )

    def close(self) -> None:
        """Close the window and stop the loop."""
        self.mlx.mlx_destroy_window(self.mlx_ptr, self.mlx_win)
        self.mlx.mlx_loop_exit(self.mlx_ptr)

    def key_handler(self, keycode: int, _: Any) -> None:
        """Handle keyboard events and quit on ESC."""
        if keycode == KEY_ESC:
            self.close()

    def destroy_handler(self, _: Any) -> None:
        """Handle window close events."""
        self.close()
