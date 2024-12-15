
def count_xmas_iterative(grid):
    """Counts 'XMAS' iteratively, checking all directions."""
    height = len(grid)
    width = len(grid[0])

    count = 0

    # Horizontal checks
    for row in grid:
        for i in range(width - 3):
            if row[i : i + 4] == "XMAS" or row[i : i + 4] == "SAMX":
                count += 1

    # Vertical checks
    for col in range(width):
        for i in range(height - 3):
            word = "".join([grid[i + j][col] for j in range(4)])
            if word == "XMAS" or word == "SAMX":
                count += 1

    # Diagonal checks (top-left to bottom-right)
    for i in range(height - 3):
        for j in range(width - 3):
            word = "".join([grid[i + k][j + k] for k in range(4)])
            if word == "XMAS" or word == "SAMX":
                count += 1

    # Diagonal checks (bottom-left to top-right)
    for i in range(3, height):
        for j in range(width - 3):
            word = "".join([grid[i - k][j + k] for k in range(4)])
            if word == "XMAS" or word == "SAMX":
                count += 1

    return count 