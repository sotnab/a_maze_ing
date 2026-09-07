*This project has been created as part of the 42 curriculum by wbaran, jazurek.*

# A Maze Ing

## Description

### Project overview

`A Maze Ing` is a project with a goal of generating mazes and visualizing them either using terminal ASCII  
representation or 42's `minilibx` graphics library. Mazes are solved what means that the shortest path is found  
and its displayed. Both maze generation and path drawing steps are animated.

Our solution uses `minilibx` which is a wrapper library for `X-window server`. It provides basic utilities  
for creating windows and images. Rendering is done on raw data using `numpy`'s ndarrays.

Logic for generating maze is separated from visualizer and is build into a package that can be reused  
later for e. g. retro games.

### Algorithms

- **Randomized Deep first search**  
The fastest one. It creates mazes with long corridors.
- **Wilson's maze algorithm**  
It uses loop-erased random walk starting from a randomly selected cell.  
Creates the most unique patterns.
- **Prim's maze algorithm**  
Very simple algorithm that creates mazes with short dead ends.

### Configuration

App provides ability to customize our mazes. Config file should
be formatted like .env file with `KEY=VALUE` pairs followed by a new line.

#### Available options

```
WIDTH=25                Maze width (number of cells)
HEIGHT=20               Maze height (number of cells)
ENTRY=0,0               Entry coordinates (x,y)
EXIT=19,7               Exit coordinates (x,y)
OUTPUT_FILE=maze.txt    Output filename
PERFECT=True            Is the maze perfect?
SEED=42                 Seed for reproducing mazes
```

## Instructions

- Run project
```bash
make
```

- Run project using python debugger `pdb`
```bash
make debug
```

- Other make rules
```bash
# Run flake8 and mypy
make lint               # Normal mode
make lint-strict        # Strict mode

# Install packages required for visualizer
make install
# Install packages required for building mazegen package
make install-mazegen

# Build mazegen package
make build

# Remove temporary and build files
make clean              # Remove cache files
make fclean             # Remove cache files, venv and mazegen packaeg

# fclean and install
make re
```

## Team

Project has been created by **wbaran** **jazurek** a part of 42's core curriculum

### Roles

- **wbaran** - Maze visualizer, Wilson's algorithm and Prim's algorithm
- **jazurek** - `Makefile`, Pathfinding algorithm, DFS algorithm


## Resources

### Web pages

- [Wikipedia's general maze generation article](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Miklix randomized deep first search](https://www.miklix.com/mazes/maze-generators/recursive-backtracker)
- [Red Blob Games pathfinding algorithms](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [Buckblog prim's maze algorithm](https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm)
- [Buckblog wilson's maze algorithm](https://weblog.jamisbuck.org/2011/1/20/maze-generation-wilson-s-algorithm)
- [Python documentation](https://docs.python.org/3/library/pydoc.html)
- [Pydantic documentation](https://pydantic.dev/docs/validation/latest/get-started/)
- [Numpy documentation](https://numpy.org/doc/)
- [Minilibx C docs](https://42-cursus.gitbook.io/guide/minilibx) - I couldn't find python version

### AI usage

- Helping with minilibx usage since there is no documentation of a python port
- Finding good python practices
- Help with displaying bitmap in mlx


## MazeGen Documentation

### Description

MazeGen is a package that contains functionality to generate mazes. Generator class `MazeGen`
provides methods to generate mazes based on config provided in file or as an argument
of type `MazeConfig`(described below). `MazeConfig` is a `pydantic` class used to validate and store
configuration. Generated `Maze` class contains hexadecimal representation of a maze,
solution which is the shortest path from entrance to exit and generation steps
that can be used for animation. Generated mazes can be either perfect or not.
Perfect maze contains only one path from entry to exit and not perfect has no dead ends.
Non-perfect maze can be used for game like Pac-Man.

### Algorithms

- `Deep first search` - Most efficient. Creates mazes with long corridors.
- `Wilson's algorithm` - Slow but creates the most unique patterns.
- `Prim's algorithm` - Creates mazes with lots of short dead ends.

### Types

Package provides type aliases for maze and utilities

```python
Cell: TypeAlias = tuple[int, int]       # Cell of a maze
Step: TypeAlias = tuple[int, int, int]  # Step of generation (x, y, cell integer representation)
Grid: TypeAlias = list[list[int]]       # Integer maze representation (Used during generation)
MazeData: TypeAlias = list[str]         # Hexadecimal char maze representation (This is final representation,
                                        #   saved to file and returned in Maze object)
```

### Classes

Classes for maze generation and config

#### Config

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

#### Maze

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

#### MazeGen

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

### Maze representation

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
