from collections import Counter

def calc_similarity(list1, list2):
    """
    Calculate the total similarity score between two lists of integers.
    The similarity score is computed by multiplying each number in list1
    by the number of times it appears in list2 and summing the results.
    """
    count2 = Counter(list2)

    return sum(num * count2[num] for num in list1)


def parse_input(file_path):
    """
    Parse the input file into two lists of integers.
    :param file_path: Path to the input file.
    :return: Two lists of integers.
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

    return list1, list2


if __name__ == "__main__":
    input_file = "inputs.txt"  # Default file path

    try:
        list1, list2 = parse_input(input_file)

        total_similarity = calc_similarity(list1, list2)

        print(f"Total Similarity Score: {total_similarity}")

    except Exception as e:
        print(f"Error: {e}")
