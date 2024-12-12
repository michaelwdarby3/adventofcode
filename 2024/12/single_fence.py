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

def calculate_region_area_and_perimeter(grid, x, y, plant_type, visited):
    """
    Perform flood-fill to calculate the area and perimeter of a region.
    :param grid: The garden grid.
    :param x: The starting x-coordinate.
    :param y: The starting y-coordinate.
    :param plant_type: The type of plant for the region.
    :param visited: A set to track visited cells.
    :return: A tuple (area, perimeter) of the region.
    """
    rows, cols = len(grid), len(grid[0])
    queue = [(x, y)]
    visited.add((x, y))
    area = 0
    perimeter = 0

    # Define directions for moving in the grid
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.pop(0)
        area += 1
        # Check neighbors to calculate perimeter and continue flood-fill
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == plant_type and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                elif grid[nx][ny] != plant_type:  # Neighbor is not part of the region
                    perimeter += 1
            else:  # Out of bounds, contributes to perimeter
                perimeter += 1

    return area, perimeter

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
                area, perimeter = calculate_region_area_and_perimeter(grid, x, y, grid[x][y], visited)
                price = area * perimeter
                total_price += price

    return total_price

if __name__ == "__main__":
    input_file = "input.txt"  # Default file path

    try:
        # Parse the garden grid
        garden_grid = parse_input(input_file)

        # Calculate the total fence price
        total_price = calculate_total_fence_price(garden_grid)

        print(f"Total price of fencing all regions: {total_price}")

    except Exception as e:
        print(f"Error: {e}")
