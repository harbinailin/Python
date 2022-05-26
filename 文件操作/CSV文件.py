import csv

with open("csv文件.csv", "w", newline="") as f:
    writer = csv.writer(f)
    test_list = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    for l in test_list:
        writer.writerow(l)

with open("csv文件.csv") as f:
    reader = csv.reader(f)
    for r in reader:
        print(r)
