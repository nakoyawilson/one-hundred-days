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

num1 = float(input("What's the first number?: "))
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = float(input("What's the second number?: "))
answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

# Continue program until user types 'n'
continue_program = "y"
while continue_program == "y":
  continue_program = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ")
  if continue_program == "y":
    num1 = answer
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  else:
    continue_program = "no"