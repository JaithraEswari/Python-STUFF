from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+':add, '-':subtract, '*':multiply, '/':divide}



def calculator_function():
    num1 = int(input("What's the number?: "))
    for symbols in operations:
        print(symbols)
    keep_going = True
    while keep_going:    
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        question = (input('Do you want to continue then type "yes" or "no" to start a new calculator: '))
        if question == 'yes':
            num1 = answer
        else:
            keep_going = False
            calculator_function()

calculator_function()