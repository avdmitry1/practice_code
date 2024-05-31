def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "divide":
        return a / b
    elif operator == "multiply":
        return a * b


print(arithmetic(8, 2, "subtract"))
