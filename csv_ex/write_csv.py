lunch = {
    '고갯마루' : '02-123-4567',
    '세븐브릭스' : '02-456-3573',
    '아랑졸돈까스' : '02-4399-5389'
}

# csv 조작법1 : string formatting
with open('lunch.csv', 'w', encoding ='utf-8') as f :
    for item in lunch.items() :
        # csv 구분은 ','
        f.write(f'{item[0]},{item[1]} \n')

# csv 조작법2 : join
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items() :
        f.write(','.join(item) + '\n')

# csv 조작법3 : csv.writer
import csv

with open('lunch.csv', 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)
