def count_x_mas(grid):
    """Counts the occurrences of 'X-MAS' (two 'MAS' in an X shape) in the grid.

    Args:
      grid: A list of strings representing the word search grid.

    Returns:
      The number of times 'X-MAS' appears in the grid.
    """
    height = len(grid)
    width = len(grid[0])
    count = 0

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if grid[y][x] == "A":
                above = grid[y - 1][x - 1] + grid[y - 1][x + 1]
                below = grid[y + 1][x - 1] + grid[y + 1][x + 1]
                if above + below in ("MMSS", "SSMM", "MSMS", "SMSM"):
                    count += 1
    return count