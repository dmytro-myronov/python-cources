import csv
import json

with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    i = 0
    student_list = []

    for row in reader:
        print(row)
        if i == 0:
            header = row
        if i > 0:
            try:
                student = dict(zip(header, row))
                student_list.append(student)
            except ValueError:
                continue
        i+=1
    with open('convert_new.json', 'w') as json_file:
        json.dump(student_list, json_file)
