# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 00:31:04 by wbaran          #+#    #+#               #
#  Updated: 2026/08/12 16:23:46 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from src.maze_config import MazeConfig
from pydantic import ValidationError
from sys import stderr


def print_config(config: MazeConfig) -> None:
    print("Width:", config.width)
    print("Height:", config.height)
    print("Entry:", config.entry)
    print("Exit:", config.exit)
    print("Output file:", config.output_file)
    print("Perfect:", config.perfect)


def main() -> None:
    try:
        config = MazeConfig.from_file("config.txt")
        print_config(config)

    except ValidationError as e:
        errors = e.errors()
        for error in errors:
            field = str(error["loc"][0]) + ":"
            print(field, error["msg"], file=stderr)

    except ValueError as e:
        print(e, file=stderr)


if __name__ == "__main__":
    main()
