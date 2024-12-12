def parse_input(file_path):
    """
    Parse the input file into ordering rules and updates.
    :param file_path: Path to the input file.
    :return: A tuple of (rules, updates).
    """
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()
            rules_section, updates_section = content.split("\n\n")

            # Parse rules
            rules = []
            for rule in rules_section.splitlines():
                x, y = map(int, rule.split("|"))
                rules.append((x, y))

            # Parse updates
            updates = []
            for update in updates_section.splitlines():
                updates.append(list(map(int, update.split(","))))

            return rules, updates
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the input file: {e}")


def is_update_valid(update, rules):
    """
    Check if an update is valid according to the rules.
    :param update: List of page numbers in the update.
    :param rules: List of ordering rules as tuples (X, Y).
    :return: True if the update respects the rules; otherwise False.
    """
    # Create a dictionary to map page numbers to their indices in the update
    index_map = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in index_map and y in index_map:  # Rule applies only if both pages are in the update
            if index_map[x] > index_map[y]:  # Check if rule is violated
                return False

    return True


def find_middle_page(update):
    """
    Find the middle page number of an update.
    :param update: List of page numbers in the update.
    :return: The middle page number.
    """
    return update[len(update) // 2]  # Get the middle element based on the original order


def main(file_path):
    # Parse the input
    rules, updates = parse_input(file_path)

    # Validate updates and calculate the sum of middle page numbers
    total_middle_pages = 0
    for update in updates:
        if is_update_valid(update, rules):
            middle_page = find_middle_page(update)
            total_middle_pages += middle_page

    return total_middle_pages


if __name__ == "__main__":
    input_file = "input.txt"  # Default file path

    try:
        # Compute the result
        result = main(input_file)

        print(f"Total sum of middle page numbers: {result}")

    except Exception as e:
        print(f"Error: {e}")
