# with open("numbers.txt", "w") as f:
#     for i in range(1, 6):
#         f.write(f"{i}\n")
#
# with open("numbers.txt", "r") as f:
#     nums = [int(a) for a in f.readlines()]
#     print(sum(nums))
#     f.seek(0)
#     for line in f:
#         if int(line)%2 == 0:
#             print(line.rstrip())

with open("numbers.txt", "r") as f:
    for line in f:
        a = f.readline().strip()

        if a == "" or a == "STOP":
            print("STOP READING")
            break
        else:
            print(a)

# f.seek(0)
#     print(f.read())