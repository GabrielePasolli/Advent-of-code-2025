
def calculate_maximum_joltage(battery_banks):
    """
    Calculates the maximum "joltage" for a set of battery banks.
    Each line represents a battery bank: it selects the highest-value battery,
    then among the batteries to its right, selects the second highest value.
    These two values are concatenated to form a number that is added to the total.
    """

    maximum_joltage = 0  # Total result
    battery_banks = battery_banks.strip().split('\n')  # Split the input into lines

    for bank in battery_banks:
        # Variables to store the two maximum values
        max_battery_1 = 0
        max_battery_2 = 0
        battery_position = 0  # Position of the first maximum

        # Find the maximum value in the row
        for i in range(0, len(bank) - 1):
            battery = int(bank[i])
            if battery > max_battery_1:
                max_battery_1 = battery
                battery_position = i  # Save the position

        # Find the second maximum to the right of the first
        for i in range(battery_position + 1, len(bank)):
            battery = int(bank[i])
            if battery > max_battery_2:
                max_battery_2 = battery

        # Concatenate the two maximum values
        bank_max_joltage = f"{max_battery_1}{max_battery_2}"
        maximum_joltage += int(bank_max_joltage)  # Add to the total

    return maximum_joltage


puzzle_input = """
"""

solution = calculate_maximum_joltage(puzzle_input)
print(f"The solution is: {solution}")
