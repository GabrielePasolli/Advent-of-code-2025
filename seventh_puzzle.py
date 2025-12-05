
import numpy as np
from scipy.signal import convolve2d


def count_accessible_rolls(grid_text):
    """
    Count paper rolls accessible by forklift using matrix operations.
    A roll is accessible if it has < 4 adjacent rolls.
    """
    lines = grid_text.strip().split('\n')
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0

    # Create binary matrix: 1 for @, 0 for .
    grid = np.zeros((rows, cols), dtype=int)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '@':
                grid[i, j] = 1

    # Kernel to count 8 neighbors (excludes center)
    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    # Convolve to count adjacent rolls
    adjacent_counts = (
        convolve2d(grid, kernel, mode='same', boundary='fill')
    )

    # Accessible: is a roll AND has < 4 neighbors
    accessible = (grid == 1) & (adjacent_counts < 4)

    return np.sum(accessible)


def visualize_accessible_rolls(grid_text):
    """
    Visualize which rolls are accessible using matrix operations.
    """
    lines = grid_text.strip().split('\n')
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0

    grid = np.zeros((rows, cols), dtype=int)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '@':
                grid[i, j] = 1

    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    adjacent_counts = (
        convolve2d(grid, kernel, mode='same', boundary='fill')
    )

    accessible = (grid == 1) & (adjacent_counts < 4)

    # Build result string
    result = []
    for i in range(rows):
        row_str = []
        for j in range(cols):
            if accessible[i, j]:
                row_str.append('x')
            elif grid[i, j] == 1:
                row_str.append('@')
            else:
                row_str.append('.')
        result.append(''.join(row_str))

    return '\n'.join(result)


# Example from the problem
puzzle_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

solution = calculate_maximum_joltage(puzzle_input, 12)
print(f"The solution is: {solution}")
