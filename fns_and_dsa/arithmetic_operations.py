def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1: first number
        num2: second number
        operation: one of 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: result of the operation, or an error message string
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
