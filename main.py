# # try:
# #     with open('secret.txt', 'r', encoding="utf-8") as f:
# #         secret = f.read()
# # except FileNotFoundError:
# #     print("secret.txt not found. Creating secret.txt")
# #     with open('secret.txt', 'w', encoding="utf-8") as f:
# #         f.write("file created")
# import sys
#
#
# # age = int(input("Введите возраст: "))
# #
# # if age < 0:
# #     raise ValueError("Возраст не может быть отрицательным")
# #
# # print("Возраст принят:", age)
#
# # try:
# #     number = int(input("Введите число: "))
# # except ValueError:
# #     print("Вы ввели не число")
# #     raise          # пробрасываем ту же ошибку дальше
#
# # a = int(input("ENTER NUMBER FROM 1 TO 10: "))
# # if a<1 or a>10:
# #     raise ValueError("NUMBER MUST BE FROM 1 TO 10")
# # else:
# #     print(a)
#
# # def get_positive(number):
# #     if number <=0:
# #         raise ValueError("Negative number")
# #     else:
# #         return number
# # print(get_positive(0))
#
# # def open_file(filename):
# #     try:
# #         if filename == "":
# #             raise ValueError
# #         else:
# #             with open(filename, "r") as f:
# #                 a = f.read()
# #                 print(a)
# #                 return a
# #     except FileNotFoundError:
# #         print("File not found")
# #         raise
# # open_file("weekday.txt")
#
# def check_dict_value(dictionary, key):
#     try:
#         # 1. Пытаемся получить значение по ключу
#         value = dictionary[key]
#
#         # 2. Пытаемся превратить его в число (float покроет и целые, и дробные)
#         number = float(value)
#
#         print(f"Успешно! Значение: {number}")
#         return number
#
#     except KeyError:
#         print(f"Ошибка: Ключа '{key}' нет в словаре.")
#
#     except ValueError:
#         print(f"Ошибка: Значение '{value}' нельзя превратить в число.")
#
#

print("w".isalpha())