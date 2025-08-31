def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == '+':
        print("The result is:", num1 + num2)
    elif operation == '-':
        print("The result is:", num1 - num2)
    elif operation == '*':
        print("The result is:", num1 * num2)
    elif operation == '/':
        if num2 != 0:
            print("The result is:", num1 / num2)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation!")


calculator()
