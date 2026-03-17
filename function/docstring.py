def average (values):
    """
    Find the mean in a sequence of values and round to two decimal places.

    Args:
        values(lists): A list of numeric values

    Returns:
        rounded_average(float): The mean of values, rounded to two decimal places.
    """

    average_value = sum(values) / len(values)

    rounded_average = round(average_value, 2)

    return rounded_average


print(average.__doc__)

print(help(average))
