import csv

summ = 0
avg = 0
maximal = None

with open("text.csv", "r", encoding="utf-8", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if maximal is None or row["score"] > maximal:
            maximal = row["score"]
        try:
            summ = summ+float(row["score"])
        except ValueError:
            continue
        cnt = sum(1 for row in reader)
        avg = summ/cnt

    print(f"AVERAGE: {avg}, MAX:{maximal}, SUM: {summ}")
with open("text.csv", "r", encoding="utf-8", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
