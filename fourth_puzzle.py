
def sum_invalid_ids(id_ranges):
    """
    Check for any ID which is made only of some sequence of digits repeated
    at least twice.
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
            if is_repetition(str(single_id)):
                output += single_id
    return output


def is_repetition(s):
    """
    Check if the string is a repetition of a smaller pattern
    by searching for it in a doubled version with ends removed.
    Example: "abcabc" -> "abcabcabcabc"[1:-1] = "bcabcabcab"
    "abcabc" is found in "bcabcabcab", so it's a repetition
    Non-repetition: "abcdef" -> "abcdefabcdef"[1:-1] = "bcdefabcde"
    "abcdef" is NOT found in "bcdefabcde", so it's not a repetition
    """
    return s in (s + s)[1:-1]


puzzle_input = """
"""

solution = sum_invalid_ids(puzzle_input)
print(f"The solution is: {solution}")
