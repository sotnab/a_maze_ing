
# MazeGen Documentation

## Description

MazeGen is a package that contains functionality to generate mazes.

## Algorithms

- `Deep first search` - Most efficient. Creates mazes with long corridors.
- `Wilson's algorithm` - Slow but creates the mos unique patterns.
- `Prim's algorithm` - Creates mazes with lots of dead ends.

## Types

Package provides classes and type aliases for maze and utilities




## Config

Package provides pydantic model `MazeConfig` for configuration.

```python
class MazeConfig(BaseModel):
    width: int = Field(ge=2, le=120)    # Maze width <2, 120>
    height: int = Field(ge=2, le=86)    # Maze height <2, 86>
    entry: Cell                         # Entry tuple[int, int]
    exit: Cell
    output_file: str
    perfect: bool = False
    seed: int | None = None
```
