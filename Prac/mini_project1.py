oper_list = ["+", "-", "*", "/"]
history = []
exit_try = ["exit", "выход"]


def sum_numbers(num1, num2):
    hst(num1, "+", num2, num1 + num2)
    return num1 + num2

def del_numbers(num1, num2):
    hst(num1, "-", num2, num1 - num2)
    return num1 - num2

def multiply_numbers(num1, num2):
    hst(num1, "*", num2, num1 * num2)
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 != 0:
        hst(num1, "/", num2, num1 / num2)
        return num1 / num2
    else:
        print("Divide by zero")
        return 0

def hst(num1, oper, num2, res):
    if len(history) < 5:
        history.append([f"{num1}{oper}{num2}={res}"])
    else:
        history.pop(0)
        history.append([f"{num1}{oper}{num2}={res}"])

def hst_check():
    for op in history:
        print(op)

print("HELLO. IT'S CALCULATOR. exit TO EXIT. HIS to check history")
while True:
    try:
        act_num = input("Enter a first number: ")
        if act_num.lower() == "exit" or act_num.lower() == "выход":
            break
        elif act_num.lower() == "his":
            hst_check()
            continue

        act_num = int(act_num)

    except ValueError:
        print("Invalid value")
    else:
        break


while True:
    try:
        operation = input("Enter operation: ")
        if operation not in oper_list:
            if operation.lower() == "exit" or operation.lower() == "выход":
                break
            elif operation.lower() == "his":
                hst_check()
                continue
            else:
                print("Invalid operation")
                continue
        else:
            new_num = input("Enter a new number: ")
            if new_num.isalpha():
                if new_num.lower() == "exit" or new_num.lower() == "выход":
                    break
                elif new_num.lower() == "his":
                    hst_check()
                    continue
            else:
                new_num = int(new_num)


        if operation == "+":
            act_num = sum_numbers(act_num, new_num)
            print(act_num)

        elif operation == "-":
            act_num = del_numbers(act_num, new_num)
            print(act_num)

        elif operation == "*":
            act_num = multiply_numbers(act_num, new_num)
            print(act_num)

        else:
            if new_num == 0:
                raise ZeroDivisionError
            else:
                act_num = divide_numbers(act_num, new_num)
                print(act_num)


    except ValueError:
        print("Invalid operation")

    except ZeroDivisionError:
        print("You can't divide by zero")
        print(act_num)

    except AttributeError:
        print("Invalid operation")
        print(act_num)






