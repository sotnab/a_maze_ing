# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_config.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 15:47:40 by wbaran          #+#    #+#               #
#  Updated: 2026/09/04 20:05:04 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from enum import Enum

from pydantic import (
    BaseModel, field_validator, ValidationError, Field
)


class Algorithm(Enum):
    DFS = "dfs"
    WILSON = "wilson"


class MazeConfig(BaseModel):
    width: int = Field(ge=2, le=120)
    height: int = Field(ge=2, le=80)
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool = False
    seed: int | None = None
    algorithm: Algorithm = Algorithm.DFS

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
