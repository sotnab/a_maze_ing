# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 00:31:04 by wbaran          #+#    #+#               #
#  Updated: 2026/09/06 15:11:47 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import ValidationError
from sys import stderr, argv

from src.maze_visualizer import MazeVisualizer
from src.maze_gen import MazeConfig


def main() -> None:
    if len(argv) != 2:
        return print("Invalid arguments. Run: ./a_maze_ing <config_file>.")

    try:
        visualizer = MazeVisualizer(argv[1])
        visualizer.show_window()

    except (ValidationError) as e:
        MazeConfig.handle_validation_error(e)

    except (ValueError, PermissionError, UnicodeDecodeError) as e:
        print(e, file=stderr)


if __name__ == "__main__":
    main()
