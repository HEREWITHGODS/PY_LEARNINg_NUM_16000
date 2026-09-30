print("HELLO, NOW YOU'RE IN MY CALCULATOR")
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
symb = input("Enter a symbol: ")
if symb == "+":
    print(f"The result of adding {num1} and {num2} is {num1 + num2}")
elif symb == "-":
    print(f"The result of subtracting {num1} and {num2} is {num1 - num2}")
elif symb == "*":
    print(f"The result of multiplying {num1} and {num2} is {num1 * num2}")
elif symb == "/":
    if num2 == 0:
        print("Division by zero. AI AI AI")
    else:
        print(f"The result of divining {num1} and {num2} is {num1 / num2}")