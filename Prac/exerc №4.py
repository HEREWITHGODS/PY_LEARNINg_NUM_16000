with open("file.txt", "r", encoding="utf-8") as f:
    cnt = 0
    for word in f.read().split():
        if word.isalpha():
            cnt += 1
    with open("result.txt", "a", encoding="utf-8") as file:
        file.write(f"Текст имеет {cnt} слова\n")

    f.seek(0)
    cnt = 0
    for letter in f.read():
        if letter.isalpha():
            cnt += 1
    with open("result.txt", "a", encoding="utf-8") as file:
        file.write(f"Текст имеет {cnt} буквы\n")

    f.seek(0)
    with open("result.txt", "a", encoding="utf-8") as file:
        file.write(f"В тексте {len(f.readlines())} строк")

