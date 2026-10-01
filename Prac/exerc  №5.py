def safe_divide(num1, num2):
    try:
        print(int(num1) / int(num2))
    except ValueError:
        print("Делить можно только числа")
    except ZeroDivisionError:
        print("На ноль делить нельзя")

num1 = input()
num2 = input()

safe_divide(num1, num2)
