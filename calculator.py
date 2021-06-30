from calculator_art import logo
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  }

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # Continue program until user types 'n' or '0'
    continue_program = "c"
    while continue_program == "c":
        continue_program = input(f"Type 'c' to continue calculating with {answer}, type 'n' to start a new calculation, or '0' to exit: ")
        if continue_program == "c":
            num1 = answer
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))
            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        elif continue_program == "n":
            continue_program = "n"
            calculator()
        else:
            continue_program = "0"

calculator()