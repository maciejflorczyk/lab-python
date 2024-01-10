# "What's the first number? "
# "Available operations: + - * /"
# "Pick an operation: "
# "What's the next number? "
# operation_string
# "Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation.

def add(n1, n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator():
    import art
    print(art.logo)
    num1 = float(input("What's the first number?  "))

    for key in operations:
        print(key)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
