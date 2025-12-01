
def solve_safe_dial(rotations_text):
    """
    Simulates dial rotations of a safe and counts how many times any click
    causes the dial to point at 0.
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

        # Count how many times we pass through 0
        if direction == 'L':
            # Count zeros while moving left
            for i in range(1, distance + 1):
                moving_position = (position - i) % 100
                if moving_position == 0:
                    zero_count += 1
            position = (position - distance) % 100

        elif direction == 'R':
            # Count zeros while moving right
            for i in range(1, distance + 1):
                moving_position = (position + i) % 100
                if moving_position == 0:
                    zero_count += 1
            position = (position + distance) % 100

    return zero_count


puzzle_input = """
"""

password = solve_safe_dial(puzzle_input)
print(f"The password is: {password}")
