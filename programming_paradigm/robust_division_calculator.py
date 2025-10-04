def safe_divide(numerator, denominator):
    """
    Attempt to divide numerator by denominator.
    Returns a string with either the result or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
