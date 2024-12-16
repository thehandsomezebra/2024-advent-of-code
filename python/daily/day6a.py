

def find_guard_position(map_grid):
  """Finds the guard's starting position on the map."""
  for row in range(len(map_grid)):
    for col in range(len(map_grid[0])):
      if map_grid[row][col] in "^v<>":
        return (row, col)
  return None

def get_guard_direction(guard_char):
  """Determines the guard's starting direction."""
  directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
  return directions.get(guard_char)

def get_next_position(current_pos, direction):
  """Calculates the next position."""
  return (current_pos[0] + direction[0], current_pos[1] + direction[1])

def turn_right(direction):
  """Turns the guard right."""
  turns = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
  return turns[direction]

def simulate_guard_path(map_grid):
  """Simulates the guard's path and counts distinct positions visited."""
  guard_pos = find_guard_position(map_grid)
  guard_dir = get_guard_direction(map_grid[guard_pos[0]][guard_pos[1]])
  visited_positions = set([guard_pos])

  while True:
    next_pos = get_next_position(guard_pos, guard_dir)
    if not (0 <= next_pos[0] < len(map_grid) and 0 <= next_pos[1] < len(map_grid[0])):
      break
    if map_grid[next_pos[0]][next_pos[1]] == "#":
      guard_dir = turn_right(guard_dir)
    else:
      guard_pos = next_pos
      visited_positions.add(guard_pos)

  return len(visited_positions)

# # Example usage
# map_grid = [
#     "....#.....",
#     ".........#",
#     "..........",
#     "..#.......",
#     ".......#..",
#     "..........",
#     ".#..^.....",
#     "........#.",
#     "#.........",
#     "......#...",
# ]
# count = simulate_guard_path(map_grid)
# print(count)  # Output: 41