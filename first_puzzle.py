
def solve_safe_dial(rotations_text):
    """
    Simulates dial rotations of a safe and counts how many times it lands on 0.
    """
    lines = rotations_text.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == 'L':
            position = (position - distance) % 100
        elif direction == 'R':
            position = (position + distance) % 100

        if position == 0:
            zero_count += 1

    return zero_count


puzzle_input = """
"""

password = solve_safe_dial(puzzle_input)
print(f"The password is: {password}")
