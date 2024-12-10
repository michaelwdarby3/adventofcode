def read_grid(file_path):
    """
    Read the word search grid from the input file.
    :param file_path: Path to the input file.
    :return: A 2D list of characters representing the grid.
    """
    try:
        with open(file_path, "r") as file:
            return [list(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the input file: {e}")

def count_x_mas(grid):
    """
    Count all occurrences of X-MAS patterns in the grid.
    :param grid: A 2D list of characters representing the word search grid.
    :return: The total count of X-MAS patterns.
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Define the diagonal offsets
    diagonals = [
        (-1, -1), (-1, 1),  # Top-left, Top-right
        (1, -1), (1, 1)     # Bottom-left, Bottom-right
    ]

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] == "A":  # Center must be "A"
                # Gather diagonal neighbors
                neighbors = [
                    (x + dx, y + dy) for dx, dy in diagonals
                    if 0 <= x + dx < rows and 0 <= y + dy < cols
                ]
                # Count M's and S's among diagonal neighbors
                m_count = sum(1 for nx, ny in neighbors if grid[nx][ny] == "M")
                s_count = sum(1 for nx, ny in neighbors if grid[nx][ny] == "S")

                # Check if there are 2 M's and 2 S's
                if m_count == 2 and s_count == 2:
                    # Check if each M has an opposite S
                    m_positions = [(nx, ny) for nx, ny in neighbors if grid[nx][ny] == "M"]
                    s_positions = [(nx, ny) for nx, ny in neighbors if grid[nx][ny] == "S"]
                    if any(
                        (mx + sx == 2 * x and my + sy == 2 * y)
                        for mx, my in m_positions
                        for sx, sy in s_positions
                    ):
                        count += 1

    return count

if __name__ == "__main__":
    input_file = "input.txt"  # Default file path

    try:
        # Read the grid from the input file
        grid = read_grid(input_file)

        # Count all X-MAS patterns
        total_x_mas = count_x_mas(grid)

        print(f"Total occurrences of X-MAS: {total_x_mas}")

    except Exception as e:
        print(f"Error: {e}")
