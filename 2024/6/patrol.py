import traceback


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
            if row:
                print(f"Processing row {r}: {row}")  # Debug statement
                grid.append(row)
                for c, char in enumerate(row):
                    if char in directions:
                        start_position = (r, c)
                        direction = directions[char]
                        print(f"Guard found at ({r}, {c}) facing {char}")  # Debug statement

    if not grid:
        raise ValueError("The map is empty.")
    if start_position is None or direction is None:
        raise ValueError("The guard's position or direction is missing.")

    return grid, start_position, direction



def simulate_guard(grid, start_position, start_direction):
    """
    Simulate the guard's movement and determine the distinct positions visited.
    :param grid: The 2D map grid.
    :param start_position: The initial position of the guard.
    :param start_direction: The initial direction of the guard.
    :return: The number of distinct positions visited.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    direction_index = directions.index(start_direction)

    visited = set()
    current_position = start_position
    visited.add(current_position)

    while True:
        r, c = current_position
        dr, dc = directions[direction_index]
        next_r, next_c = r + dr, c + dc

        # Check if the guard is about to leave the grid
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        # Check if the next cell is within bounds before accessing
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '#':
            direction_index = (direction_index + 1) % 4  # Turn right
        else:  # Move forward
            current_position = (next_r, next_c)
            visited.add(current_position)

    return len(visited)

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your file path

    try:
        # Parse the map
        grid, start_position, start_direction = parse_map(input_file)

        # Simulate the guard's movement
        distinct_positions = simulate_guard(grid, start_position, start_direction)

        print(f"Number of distinct positions visited: {distinct_positions}")

    except Exception as e:
        print(f"Error: {e}")
        print(f"Traceback: {traceback.format_exc()}")
