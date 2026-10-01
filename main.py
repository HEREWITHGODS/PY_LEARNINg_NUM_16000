from datetime import datetime

with open("poem.txt", "w", encoding="utf-8") as f:
    f.write("Я  ПОМНЮ ЧУДНОЕ МГНОВЕНЬЕ\n")
    f.write("ПЕРЕДО МНОЙ ЯВИЛОСЬ ТЫ\n")
    f.write("КАК МИМОЛЁТНОЕ ВИДЕНИЕ\n")
    f.write("КАК ГЕНИЙ ЧИСТОЙ КРАСОТЫ\n")

weekday = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
for i in range(len(weekday)):
    weekday[i] = weekday[i]+"\n"

with open("weekday.txt", "w", encoding="utf-8") as f:
    f.writelines(weekday)

now = datetime.now()
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(str(now)+"\n")