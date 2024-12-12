def parse_map(file_path):
    """
    Parse the map input to extract the grid, the guard's initial position, and direction.
    :param file_path: Path to the input file.
    :return: A tuple (grid, start_position, direction).
    """
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    grid = []
    start_position = None
    direction = None

    with open(file_path, "r") as file:
        for r, line in enumerate(file):
            row = list(line.strip())
            grid.append(row)
            for c, char in enumerate(row):
                if char in directions:
                    start_position = (r, c)
                    direction = directions[char]

    if not grid or start_position is None or direction is None:
        raise ValueError("Invalid or empty map input.")

    return grid, start_position, direction

def simulate_guard(grid, start_position, start_direction):
    """
    Simulate the guard's movement and determine if they leave the grid or get stuck in a loop.
    :param grid: The 2D map grid.
    :param start_position: The initial position of the guard.
    :param start_direction: The initial direction of the guard.
    :return: A tuple (exited, visited_positions).
             - exited: True if the guard exits the grid, False if they get stuck in a loop.
             - visited_positions: The set of positions and directions visited.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = directions.index(start_direction)

    visited = set()
    current_position = start_position
    visited.add((current_position, direction_index))

    while True:
        r, c = current_position
        dr, dc = directions[direction_index]
        next_r, next_c = r + dr, c + dc

        # Check if the guard is about to leave the grid
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            return True, visited  # Guard exits the grid

        # Check the cell in front of the guard
        if grid[next_r][next_c] == '#':  # Obstacle in front
            direction_index = (direction_index + 1) % 4  # Turn right
        else:  # Move forward
            current_position = (next_r, next_c)
            if (current_position, direction_index) in visited:
                return False, visited  # Guard is stuck in a loop
            visited.add((current_position, direction_index))

def find_valid_obstruction_positions(grid, start_position, start_direction):
    """
    Find all positions where placing a single obstruction would cause the guard to get stuck in a loop.
    :param grid: The 2D map grid.
    :param start_position: The initial position of the guard.
    :param start_direction: The initial direction of the guard.
    :return: The count of valid obstruction positions.
    """
    rows, cols = len(grid), len(grid[0])
    valid_positions = 0

    for r in range(rows):
        for c in range(cols):
            # Skip starting position and existing obstacles
            if (r, c) == start_position or grid[r][c] == '#':
                continue

            # Temporarily place an obstruction
            original_value = grid[r][c]
            grid[r][c] = '#'

            # Simulate guard movement
            exited, _ = simulate_guard(grid, start_position, start_direction)

            # If the guard gets stuck in a loop, this is a valid position
            if not exited:
                valid_positions += 1

            # Restore the original value
            grid[r][c] = original_value

    return valid_positions

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your file path

    try:
        # Parse the map
        grid, start_position, start_direction = parse_map(input_file)

        # Find valid obstruction positions
        valid_obstruction_count = find_valid_obstruction_positions(grid, start_position, start_direction)

        print(f"Number of valid obstruction positions: {valid_obstruction_count}")

    except Exception as e:
        print(f"Error: {e}")
