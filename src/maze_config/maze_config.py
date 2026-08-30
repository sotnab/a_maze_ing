# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_config.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 15:47:40 by wbaran          #+#    #+#               #
#  Updated: 2026/08/13 12:37:47 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pydantic import BaseModel, field_validator, ValidationError


class MazeConfig(BaseModel):
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool = False
    seed: int | None = None

    @field_validator("entry", "exit", mode="before")
    @classmethod
    def validate_coords(cls, value: str) -> tuple[int, int]:
        splitted = value.split(",")
        if len(splitted) != 2:
            raise ValidationError("Entry and exit should be formatted: x,y")

        return (int(splitted[0]), int(splitted[1]))

    @classmethod
    def from_file(cls, filename: str) -> "MazeConfig":
        config = {}

        with open(filename, encoding="utf-8") as file:
            for line in file:
                if line.startswith(("#", "\n")):
                    continue

                splitted = line.strip().split("=")
                if len(splitted) != 2:
                    raise ValueError("Config file is in invalid format")

                key, value = splitted
                config[key.lower()] = value

        return cls.model_validate(config)
