import csv

with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    i = 0
    grade_list = []

    for row in reader:
        print(row)
        if i > 0:
            try:
                grade_list.append(float(row[1]))
            except ValueError:
                continue
        i+=1
    print("avg students grade: " + str(sum(grade_list) / len(grade_list)))