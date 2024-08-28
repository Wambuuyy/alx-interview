```markdown
# Island Perimeter

## Description

This project contains a Python function, `island_perimeter`, that calculates the perimeter of an island within a given 2D grid. The grid is represented as a list of lists of integers where:
- `0` represents water
- `1` represents land

The function computes the perimeter of the single island in the grid, which is entirely surrounded by water.

## Function

### `island_perimeter(grid)`

**Arguments:**
- `grid` (List[List[int]]): A 2D list where each element is either `0` (water) or `1` (land). The grid is rectangular, and its width and height do not exceed 100.

**Returns:**
- `int`: The perimeter of the island.

**Example:**

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x09-island_perimeter
   ```

3. Ensure the script is executable and run the test script:

   ```bash
   chmod +x 0-main.py
   ./0-main.py
   ```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Feel free to customize the URLs and project details as needed!