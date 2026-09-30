#smart calculator 

#get input from user

number_1 = float(input("Enter a number? "))
number_2 = float(input("Enter another number? "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = number_1 + number_2
    print(f"Result = {result}")

elif operation == "-":
    result = number_1 - number_2
    print(f"Result = {result}")

elif operation == "*":
    result = number_1 * number_2
    print(f"Result = {result}")

elif operation == "/":
    if  number_2 == 0:
        print("number cant be divided")
    else:
        result = number_1 / number_2
        print(f"Result = {result}")

else:
    print("Please enter a valid operator")