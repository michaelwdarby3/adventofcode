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

def find_word(grid, word):
    """
    Count all occurrences of a word in the grid, considering all directions.
    :param grid: A 2D list of characters representing the word search grid.
    :param word: The word to search for.
    :return: The total count of occurrences of the word.
    """
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def is_valid(x, y, dx, dy):
        """
        Check if the word can fit starting at (x, y) in the given direction.
        """
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x, y, dx, dy):
                    count += 1

    return count

if __name__ == "__main__":
    input_file = "input.txt"  # Default file path
    word_to_find = "XMAS"

    try:
        # Read the grid from the input file
        grid = read_grid(input_file)

        # Find and count all occurrences of the word
        total_occurrences = find_word(grid, word_to_find)

        print(f"Total occurrences of '{word_to_find}': {total_occurrences}")

    except Exception as e:
        print(f"Error: {e}")
