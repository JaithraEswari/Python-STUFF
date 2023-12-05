def findNthNumber(n):
    # Check if n is within the valid range
    if n < 1 or n > 50:
        raise ValueError("Invalid value for n. It should be between 1 and 50.")

    # Initialize the first four numbers in the series
    n1, n2, n3, n4 = 1, 2, 3, 4

    # Handle special cases for n=1 to n=4
    if n == 1:
        return n1
    elif n == 2:
        return n2
    elif n == 3:
        return n3
    elif n == 4:
        return n4

    # Calculate the nth number using the recurrence relation
    for _ in range(5, n + 1):
        next_number = n1 + n2 + n3 + n4
        n1, n2, n3, n4 = n2, n3, n4, next_number

    return n4

# Example usage:
n = 6
result = findNthNumber(n)
print(f"The {n}th number in the series is: {result}")
