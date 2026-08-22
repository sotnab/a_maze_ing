# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 00:31:04 by wbaran          #+#    #+#               #
#  Updated: 2026/08/22 15:48:22 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import ValidationError
from sys import stderr, argv

from src import MazeConfig
from src import MazeVisualizer


class AMazeIng:
    config: MazeConfig
    visualizer: MazeVisualizer

    def __init__(self, filename: str) -> None:
        self.load_config(filename)

    def load_config(self, filename: str) -> None:
        self.config = MazeConfig.from_file(filename)

    def run(self) -> None:
        print("Running")
        self.visualizer = MazeVisualizer(self.config)
        self.visualizer.run()


def main() -> None:
    if len(argv) != 2:
        return print("Invalid arguments. Run: ./a_maze_ing <config_file>.")

    try:
        filename = argv[1]
        a_maze_ing = AMazeIng(filename)
        a_maze_ing.run()

    except (ValidationError) as e:
        errors = e.errors()
        for item in errors:
            print(item, file=stderr)

    except (ValueError, PermissionError, UnicodeDecodeError) as e:
        print(e, file=stderr)


if __name__ == "__main__":
    main()
