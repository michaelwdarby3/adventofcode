def calc_distances(list1, list2):
    """
    Calculate the total distance between two lists of integers.
    Lists are sorted before calculating distances.
    """

    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    return sum(abs(i - j) for i, j in zip(sorted_list1, sorted_list2))

def process_input(file_path):
    """
    Parse the input file and calculate the total distance between the two lists.
    :param file_path: Path to the input file.
    :return: Total distance between the two lists.
    """

    list1, list2 = [], []

    try:
        with open(file_path, "r") as f:
            for line in f:
                nums = line.strip().split()

                if len(nums) != 2:
                    raise ValueError(f"Malformed line: {line}")

                list1.append(int(nums[0]))
                list2.append(int(nums[1]))

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")

    except ValueError as e:
        raise ValueError(f"Error processing input file: {e}")

    return calc_distances(list1, list2)

if __name__ == "__main__":
    input_file = "inputs.txt"  # Default file path

    try:
        total_distance = process_input(input_file)
        print(f"Total Distance: {total_distance}")
    except Exception as e:
        print(f"Error: {e}")

