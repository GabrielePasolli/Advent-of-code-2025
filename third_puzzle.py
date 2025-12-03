
def sum_invalid_ids(id_ranges):
    """
    Check for any ID which is made only of some sequence of digits repeated
    twice.
    Args: a string wich cointains a list of id ranges
    """
    output = 0
    # Split the input string into individual range strings
    id_ranges = id_ranges.split(',')

    for id_range in id_ranges:
        # Split each range into start and end values
        id_range = id_range.split('-')

        # Iterate through all IDs in the current range
        for single_id in range(int(id_range[0]), int(id_range[1]) + 1):
            single_id = str(single_id)
            length = len(single_id)
            # Skip IDs with odd number of digits
            if length % 2 != 0:
                continue
            # Find the midpoint of the string
            mid = length // 2
            # Check if the first half equals the second half
            if single_id[:mid] == single_id[mid:]:
                output += int(single_id)
    return output


puzzle_input = """
"""

solution = sum_invalid_ids(puzzle_input)
print(f"The solution is: {solution}")
