# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 00:31:04 by wbaran          #+#    #+#               #
#  Updated: 2026/08/12 16:47:52 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from src.maze_config import MazeConfig
from pydantic import ValidationError
from sys import stderr, argv


# Temporary config printing
def print_config(config: MazeConfig) -> None:
    print("Width:", config.width)
    print("Height:", config.height)
    print("Entry:", config.entry)
    print("Exit:", config.exit)
    print("Output file:", config.output_file)
    print("Perfect:", config.perfect)


class AMazeIng:
    config: MazeConfig

    def __init__(self, filename: str) -> None:
        self.load_config(filename)
        print_config(self.config)

    def load_config(self, filename: str) -> None:
        self.config = MazeConfig.from_file(filename)

    def run(self) -> None:
        print("Running")


def main() -> None:
    if len(argv) != 2:
        return print("Invalid arguments. "
                     "Run using: ./a_maze_ing <config_file>.")

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
