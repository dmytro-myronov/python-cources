import csv


def add_new_student(student_name, student_age, student_mark):
    with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
        if is_student_exist(student_name):
            print("student with this name already exist")
            return
        writer = csv.writer(file)
        writer.writerow([student_name, student_age, student_mark])
        print("student added successfully")


def is_student_exist(student_name):
    with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        i = 0

        for row in reader:
            if i > 0:
                try:
                    if row[0] == student_name:
                        return True
                except ValueError:
                    continue
            i += 1

    return False


try:
    st_name = input("Enter student's name: ")
    st_age = int(input("Enter student's age: "))
    st_mark = float(input("Enter student's mark: "))
    if 20 > len(st_name) >= 3 and 70 > st_age > 17 and 99 > st_mark > 0:
        add_new_student(st_name, st_age, st_mark)
    else:
        print("please provide valid data. Name must be between 3 and 20. Age must be between 17 and 70. Mark between 0 and 99 ")

except ValueError as e:
    print(f"enter valid data {e}")
