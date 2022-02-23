while True:
    operation = input('''
    Please type in the math operation you would like to 
    complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    if operation == "exit":
        break
    number = float(input("Number: "))
    number2 = float(input("Number: "))
    if operation == "+":
        print(number, "+", number2, "=", number + number2)
    elif operation == "-":
        print(number, "-", number2, "=", number - number2)
    elif operation == "*":
        print(number, "*", number2, "=", number * number2)
    elif operation == "/":
        print(number, "/", number2, "=", number / number2)


   
