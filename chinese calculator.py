def calculator():
    print("Welcome to the calculator!") #first step
    print("Enter 'q' to quit the calculator.")

    while True:
        num1 = input("Enter the first number: ") #1
        if num1.lower() == 'q':
            break

        operation = input("Enter an operation (+, -, *, /): ") #operations
        if operation.lower() == 'q':
            break

        num2 = input("Enter the second number: ") #2
        if num2.lower() == 'q':
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
            continue

        int_result = int(result)
        #special codes
        if int_result == 520:
            print("I love you")
        elif int_result == 883:
            print("Lovesickness is just for you.")
        elif int_result == 222:
            print("See you at the usual place.")
        elif int_result == 444:
            print("Love you and miss you for a long time.")
        elif int_result == 605:
            print("To be faithful forever.")
        elif int_result == 11:
            print("You and I are forever.")
        elif int_result == 36:
            print("I miss you all the time.")
        else:
            print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()

