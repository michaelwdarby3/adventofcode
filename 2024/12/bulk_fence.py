from collections import deque

def parse_input(file_path):
    """
    Parse the input file to create a 2D grid representing the garden plots.
    :param file_path: Path to the input file.
    :return: A 2D list of characters representing the garden plots.
    """
    try:
        with open(file_path, "r") as file:
            return [list(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the input file: {e}")

def calculate_region_area_and_sides(grid, x, y, plant_type, visited):
    """
    Perform flood-fill to calculate the area and sides of a region.
    :param grid: The garden grid.
    :param x: The starting x-coordinate.
    :param y: The starting y-coordinate.
    :param plant_type: The type of plant for the region.
    :param visited: A set to track visited cells.
    :return: A tuple (area, sides) of the region.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(x, y)])
    visited.add((x, y))
    area = 0
    sides = 0

    # Directions for moving in the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        area += 1

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] != plant_type:
                    sides += 2  # Fence separating regions; count twice
                elif (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
            else:
                sides += 1  # Fence at the grid boundary contributes one side

    return area, sides

def calculate_total_fence_price(grid):
    """
    Calculate the total price of fencing all regions in the garden plot.
    :param grid: The garden grid.
    :return: The total price of fencing.
    """
    visited = set()
    total_price = 0

    rows, cols = len(grid), len(grid[0])
    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:  # New region
                area, sides = calculate_region_area_and_sides(grid, x, y, grid[x][y], visited)
                price = area * sides
                total_price += price

    return total_price

if __name__ == "__main__":
    input_file = "input.txt"  # Path to the user's uploaded file

    try:
        # Parse the garden grid
        garden_grid = parse_input(input_file)

        # Calculate the total fence price
        total_price = calculate_total_fence_price(garden_grid)

        print(f"Total price of fencing all regions: {total_price}")

    except Exception as e:
        print(f"Error: {e}")
