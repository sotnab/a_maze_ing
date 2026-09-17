
# MazeGen Documentation

## Description

MazeGen is a package that contains functionality to generate mazes. Generator class `MazeGen`
provides methods to generate mazes based on config provided in file or as an argument
of type `MazeConfig`(described below). `MazeConfig` is a `pydantic` class used to validate and store
configuration. Generated `Maze` class contains hexadecimal representation of a maze,
solution which is the shortest path from entrance to exit and generation steps
that can be used for animation. Generated mazes can be either perfect or not.
Perfect maze contains only one path from entry to exit and not perfect has no dead ends.
Non-perfect maze can be used for game like Pac-Man.

## Algorithms

- `Deep first search` - Most efficient. Creates mazes with long corridors.
- `Wilson's algorithm` - Slow but creates the most unique patterns.
- `Prim's algorithm` - Creates mazes with lots of short dead ends.

## Types

Package provides type aliases for maze and utilities

```python
Cell: TypeAlias = tuple[int, int]       # Cell of a maze
Step: TypeAlias = tuple[int, int, int]  # Step of generation (x, y, cell integer representation)
Grid: TypeAlias = list[list[int]]       # Integer maze representation (Used during generation)
MazeData: TypeAlias = list[str]         # Hexadecimal char maze representation (This is final representation,
                                        #   saved to file and returned in Maze object)
```

## Classes

Classes for maze generation and config

### Config

Class `MazeConfig` is a `pydantic` model used for configuration.

```python
class MazeConfig(BaseModel):
    width: int = Field(ge=2, le=120)    # Maze width <2, 120>
    height: int = Field(ge=2, le=86)    # Maze height <2, 86>
    entry: Cell                         # Maze entrance
    exit: Cell                          # Maze exit
    output_file: str                    # Output file name
    perfect: bool = False               # Maze with no dead ends(default is False)
    seed: int | None = None             # Seed (Optional)
```

MazeConfig has a method `MazeConfig.from_file(filename: str) -> MazeConfig` for reading configuration from file.
Configuration in file should be in format `KEY=VALUE` followed by a new line. Same as in .env files.

### Maze

Class `Maze` is class representing generated maze.

```python
@dataclass
class Maze:
    data: MazeData          # Maze hexadecimal representation
    width: int              # Maze width
    height: int             # Maze height
    entry: Cell             # Maze entrance
    exit: Cell              # Maze exit
    solution: list[Cell]    # Solution -> Path from entry to exit
    steps: list[Step]       # Steps of generation.
```

### MazeGen

Class `MazeGen` is the core class that is used to generate mazes.
We simply instantiate class without any parameters. It can also save
maze to file.

```python
gen = MazeGen()
```

For each algorithm we have method to generate maze.
They take `MazeConfig` and return generated `Maze` object.
There is also method `save_to_file` that is saving our maze
in hexadecimal representation to specified file.

```python
def dfs(self, config: MazeConfig) -> Maze

def wilson(self, config: MazeConfig) -> Maze

def prims(self, config: MazeConfig) -> Maze

def save_to_file(self, maze: Maze, filename: str) -> None
```

## Maze representation

Generated maze is represented as a two-dimensional array of characters.
Each character is a digit in a hexadecimal format.

One digit in hexadecimal format is 4 bits. Each bit represents a wall.

```
    Bits from right to left represent:
    - North wall
    - East wall
    - South wall
    - West wall

    0₁₆ == 0₁₀ == 0000₂ -> Cell without walls
    f₁₆ == 16₁₀ == 1111₂ -> Closed cell with four walls
    a₁₆ == 10₁₀ == 1010₂ -> Cell with east and west wall

    and so on...
```

