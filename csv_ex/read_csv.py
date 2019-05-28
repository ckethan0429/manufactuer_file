# 1. split / strip(공백제거 , rstrip, lstrip)
# with open('lunch.csv', 'r', encoding = 'utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip().split(','))

# 2. csv.reader
import csv
with open('lunch.csv', 'r', encoding = 'utf-8') as f:
    items = csv.reader(f)
    for item in items :
        print(item)