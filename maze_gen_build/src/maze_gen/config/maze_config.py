# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  maze_config.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: wbaran <wbaran@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/08/12 15:47:40 by wbaran          #+#    #+#               #
#  Updated: 2026/09/07 21:37:43 by wbaran          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from sys import stderr

from pydantic import (
    BaseModel, field_validator,
    ValidationError, Field,
    model_validator
)

from ..types import Cell


class MazeConfig(BaseModel):
    """Validate and store maze configuration data."""

    width: int = Field(ge=2, le=120)
    height: int = Field(ge=2, le=86)
    entry: Cell
    exit: Cell
    output_file: str
    perfect: bool = False
    seed: int | None = None

    def validate_position(self, cell: Cell) -> bool:
        """Check whether the cell is inside the maze bounds."""
        x, y = cell

        return (0 <= x < self.width and 0 <= y < self.height)

    @model_validator(mode="after")
    def validate_bounds(self) -> "MazeConfig":
        """Ensure the entry and exit are valid and distinct."""

        if self.entry == self.exit:
            raise ValueError("Entry and exit are the same")

        if not self.validate_position(self.entry):
            raise ValueError("Entrance outside of maze bounds")

        if not self.validate_position(self.exit):
            raise ValueError("Exit outside of maze bounds")

        return self

    @field_validator("entry", "exit", mode="before")
    @classmethod
    def validate_coords(cls, value: str) -> Cell:
        """Parse a coordinate string into a cell tuple."""

        splitted = value.split(",")

        if len(splitted) != 2:
            raise ValidationError("Entry and exit should be formatted: x,y")

        return (int(splitted[0]), int(splitted[1]))

    @classmethod
    def from_file(cls, filename: str) -> "MazeConfig":
        """Load maze settings from a configuration file."""

        config: dict[str, str] = {}

        with open(filename, encoding="utf-8") as file:

            for line in file:
                cls.parse_line(config, line)

        return cls.model_validate(config)

    @staticmethod
    def parse_line(config: dict[str, str], line: str) -> None:
        """Add a key/value pair from a config line."""

        if line.startswith(("#", "\n")):
            return

        splitted = line.strip().split("=")

        if len(splitted) != 2:
            raise ValueError("Config file is in invalid format")

        key, value = splitted

        config[key.lower()] = value

    @staticmethod
    def handle_validation_error(error: ValidationError) -> None:
        """Print readable validation errors to stderr."""
        errors = error.errors()

        for item in errors:
            loc = item["loc"]

            if len(loc):
                print(str(loc[0]).capitalize(), end=": ", file=stderr)

            print(item["msg"], file=stderr)
