import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operator_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = float(input("What is the first number?: "))

while True:
    print('+\n-\n*\n/')
    operator = input("Pick an operation: ")
    num2 = float(input("What is the second number?: "))
    result = 0.0
    if operator == '+':
        result = operator_dict[operator](num1, num2)
    elif operator == '-':
        result = operator_dict[operator](num1, num2)
    elif operator == '*':
        result = operator_dict[operator](num1, num2)
    elif operator == '/':
        result = operator_dict[operator](num1, num2)

    print(f"{num1} + {num2} = {result}")
    cont_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if cont_cal=='y':
        num1 = result
        continue
    else:
        break