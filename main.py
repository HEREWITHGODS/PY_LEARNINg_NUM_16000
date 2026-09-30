slovo = input("Enter the word: ")
cnt = 0
for c in slovo:
    if c.isalpha():
        cnt += 1
    else:
        break
else:
    print(cnt,"letter in word")