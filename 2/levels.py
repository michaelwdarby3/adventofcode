def is_safe_report(report):
    """
    Check if a single report is safe based on the given rules.
    A report is safe if levels are all increasing or decreasing,
    and any two adjacent levels differ by at least 1 and at most 3.
    """
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))

    return increasing or decreasing


def check_safety(levels):
    """
    Check how many reports are safe in the given list of reports.
    :param levels: A list of lists, where each inner list represents a report.
    :return: The number of safe reports.
    """
    return sum(1 for report in levels if is_safe_report(report))


def parse_input(file_path):
    """
    Parse the input file into a list of reports.
    Each report is a list of integers.
    :param file_path: Path to the input file.
    :return: A list of reports.
    """
    levels = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                nums = [int(i) for i in line.strip().split()]
                levels.append(nums)

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")

    except ValueError as e:
        raise ValueError(f"Error processing input file: {e}")

    return levels


if __name__ == "__main__":
    input_file = "input.txt"  # Default file path

    try:
        levels = parse_input(input_file)

        total_safe = check_safety(levels)

        print(f"Safe reports: {total_safe}")

    except Exception as e:
        print(f"Error: {e}")
