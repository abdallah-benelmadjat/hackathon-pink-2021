import csv

firstScore=int(input('1'))
secondScore=int(input('2'))
thirdScore=int(input('3'))

list = [firstScore, secondScore, thirdScore]

with open('test.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')

# skip the header of your csv
    next(reader)

    for row in reader:
        if list[0] == int(row[1]) and list[1] == int(row[2]) and list[2] == int(row[3]):
            print(row[0])
            break
        else:
            print("No match found..")
