import csv

with open("crypto_listf.csv", newline="") as f:
    reader = csv.reader(f)
    shit_list=list(reader)

crypto_list=shit_list[0]
