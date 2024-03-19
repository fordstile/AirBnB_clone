#!/usr/bin/python3
def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers (list of int or float): A list of numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total


def main():
    """Main function."""
    numbers = [1, 2, 3, 4, 5]
    total_sum = calculate_sum(numbers)
    print("The sum of the numbers is:", total_sum)


if __name__ == "__main__":
    main()
