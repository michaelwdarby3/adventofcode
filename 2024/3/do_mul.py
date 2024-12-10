import re


def parse_and_compute_with_conditions(memory):
    """
    Parse the corrupted memory and compute the sum of valid mul(X,Y) instructions,
    considering the effects of do() and don't() instructions.
    :param memory: String containing the corrupted memory.
    :return: Total sum of results from valid and enabled mul(X,Y) instructions.
    """
    # Regular expression to match mul(X,Y), do(), and don't() instructions
    pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

    # Find all instructions in the memory
    matches = re.finditer(pattern, memory)

    # Initial state: mul instructions are enabled
    mul_enabled = True
    total = 0

    for match in matches:
        instruction = match.group(0)

        if instruction.startswith("mul(") and mul_enabled:
            # Extract numbers from mul(X,Y)
            x, y = int(match.group(2)), int(match.group(3))
            total += x * y
            print(f"Processing {instruction}: Enabled -> {x} * {y} = {x * y}")
        elif instruction == "do()":
            mul_enabled = True
            print(f"Processing {instruction}: Enabling mul instructions")
        elif instruction == "don't()":
            mul_enabled = False
            print(f"Processing {instruction}: Disabling mul instructions")
        else:
            print(f"Ignored {instruction}")

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

        # Compute the total sum of valid and enabled mul instructions
        result = parse_and_compute_with_conditions(memory)

        print(f"Total sum of valid and enabled mul instructions: {result}")

    except Exception as e:
        print(f"Error: {e}")
