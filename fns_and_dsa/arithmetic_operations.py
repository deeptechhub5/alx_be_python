# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1 (float): first number
        num2 (float): second number
        operation (str): one of 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: numeric result for valid operations,
                      or an error message string for invalid operation or division by zero.
    """
    if not isinstance(operation, str):
        return "Error: Invalid operation."

    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
