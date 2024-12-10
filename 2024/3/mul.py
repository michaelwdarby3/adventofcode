import re


def parse_and_compute(memory):
    """
    Parse the corrupted memory and compute the sum of all valid mul(X,Y) instructions.
    :param memory: String containing the corrupted memory.
    :return: Total sum of results from valid mul(X,Y) instructions.
    """
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches in the memory
    matches = re.findall(pattern, memory)

    # Compute the sum of products
    total = sum(int(x) * int(y) for x, y in matches)

    return total


def read_input(file_path):
    """
    Read the contents of the input file.
    :param file_path: Path to the input file.
    :return: String containing the file content.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the input file: {e}")


if __name__ == "__main__":
    input_file = "input.txt"  # Default file path

    try:
        # Read corrupted memory from the input file
        memory = read_input(input_file)

        # Compute the total sum of valid mul instructions
        result = parse_and_compute(memory)

        print(f"Total sum of valid mul instructions: {result}")

    except Exception as e:
        print(f"Error: {e}")
