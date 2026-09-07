*This project has been created as part of the 42 curriculum by wbaran, jazurek.*

# A-Maze-ing

## Description

This project creates mazes, solves them, and displays the result in a window.  
The main goal is to generate a maze from a configuration file, find the shortest path from the entry to the exit,  
and animate the building process with a visual interface.

The project is divided into two parts:

- a reusable maze generation library called `maze_gen`
- a visualizer built on top of Python and the MinilibX graphic system

The program can generate mazes using different algorithms, save the result to a text file, and show the maze step by step.  
It also lets the user view the solved path and switch colors or animations while the window is running.

### Features

- Maze generation with 3 algorithms: DFS, Wilson, and Prim
- BFS Pathfinding to find the shortest route from entry to exit
- Maze animation while it is being built
- Path animation after the maze is ready
- Configurable maze size, entry, exit, file output, and optional seed
- Reusable generation logic separated from the drawing code

## Instructions

### Requirements

This project is designed for a Linux environment and uses Python 3.10+ with a virtual environment.

### Install and run

Before running project first you have to build maze_gen package.
From the project root, run:

```bash
make build
```

After building run using:

```bash
make
```

This command creates the virtual environment, installs dependencies,  
and starts the program with the default config file.

Other commands:

```bash
make install          # install dependencies
make install-mazegen  # install dependencies for the maze generator package
make debug            # run with Python debugger
make lint             # run flake8 and mypy
make lint-strict      # stricter static checks
make clean            # remove cache files
make fclean           # remove venv and generated package files
make re               # clean and reinstall everything
```

### How to run the visualizer

```bash
./a_maze_ing.py config.txt
```

The visualizer accepts a config file as a parameter. The default project file is `config.txt`.

### Controls in the window

- `1` : generate a maze with DFS
- `2` : generate a maze with Wilson's algorithm
- `3` : generate a maze with Prim's algorithm
- `4` : show or hide the path
- `5` : skip the current animation
- `6` : return to the title screen
- `7` : switch wall colors

## Config file structure

The config file is plain text and follows a simple `KEY=VALUE` format.  
One option per line. Empty lines and lines starting with `#` are ignored.

Example from the project:

```ini
# Maze width (number of cells)
WIDTH=25

# Maze height
HEIGHT=20

# Entry coordinates (x,y)
ENTRY=1,1

# Exit coordinates (x,y)
EXIT=19,14

# Output filename
OUTPUT_FILE=maze.txt

# Is the maze perfect?(no dead ends if False)
PERFECT=False

# Random seed for reproducible mazes
SEED=42
```

Notes:

- `WIDTH` must be between 2 and 120.
- `HEIGHT` must be between 2 and 86.
- Entry and exit must stay inside the maze bounds.
- Entry and exit cannot be the same cell.
- Values are validated through Pydantic models before execution.

## Chosen maze generation algorithm

We chose the iterative Depth-First Search algorithm for the default one.

### Why this algorithm?

- It is fast and easy to implement.
- It produces a maze with long corridors and a clear path structure.
- It is reliable for animation because it builds the maze step by step.

In the project, the full implementation is not the classic recursive version.  
It is an iterative version that keeps the same logic but avoids recursion depth issues on larger mazes.

### Other algorithms included

- `Wilson's algorithm`: good for more random and unique structures, but slower.
- `Prim's algorithm`: creates mazes with shorter branches and a different visual style.

## Reusable code

A large part of the project is designed to be reused outside the graphic window.

The `maze_gen` package contains:

- `MazeConfig`: validation and configuration management
- `Maze`: generated maze data, solution, and animation steps
- `MazeGen`: entry point for generating mazes
- Typealiases

See `maze_gen` documentation below for more details

## Project management and teamwork

The project was done by two students from the 42 curriculum:

- **wbaran**: maze visualization, UI integration, Wilson and Prim algorithms
- **jazurek**: project automation with `Makefile`, solver logic, DFS implementation

### Planning

At the beginning, we split the work between the maze generation library and the display layer.  
The core idea was to keep generation logic independent from the graphics, which helped later when we had to add algorithms.

### What worked well

- clear separation between logic and rendering
- modular code structure
- ability to animate generation and solution steps

### What could be improved

- more formal testing for edge cases
- a better way of handling window and rendering errors

### Tools used

- Python 3
- Pydantic for validation
- NumPy for image data processing
- MinilibX for the graphical interface
- Makefile for project automation
- Git and GitHub for version control

## Resources

### References

- [Wikipedia: Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Miklix: Recursive backtracker maze generation](https://www.miklix.com/mazes/maze-generators/recursive-backtracker)
- [Red Blob Games: A* and pathfinding](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [Jamis Buck: Prim's algorithm](https://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm)
- [Jamis Buck: Wilson's algorithm](https://weblog.jamisbuck.org/2011/1/20/maze-generation-wilson-s-algorithm)
- [Python documentation](https://docs.python.org/3/library/pydoc.html)
- [Pydantic documentation](https://docs.pydantic.dev/)
- [NumPy documentation](https://numpy.org/doc/)
- [MinilibX documentation](https://42-cursus.gitbook.io/guide/minilibx)

### AI usage

AI was useful for:

- understanding how to work with MinilibX in Python
- improving code structure and Python practices
- helping with image rendering and display logic
- checking for mistakes in algorithm and data flow 

## MazeGen Documentation

### Description

maze_gen is a package that contains functionality to generate mazes. Generator class `MazeGen`
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

