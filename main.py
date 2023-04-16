import csv
def read_data(file_name):
    students = {}
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            email = row[0]
            first_name = row[1]
            last_name = row[2]
            points = int(row[3])
            grade = row[4] if len(row) > 4 else ''
            status = row[5] if len(row) > 5 else ''
            students[email] = {'first_name': first_name, 'last_name': last_name, 'points': points, 'grade': grade, 'status': status}
    return students

def grades(students):
    for email, student in students.items():
        if student['status'] not in ['GRADED', 'MAILED']:
            points = student['points']
            if points >= 91:
                grade = 5.0
            elif points >= 81:
                grade = 4.5
            elif points >= 71:
                grade = 4.0
            elif points >= 61:
                grade = 3.5
            elif points >= 51:
                grade = 3.0
            else:
                grade = 2.0
            student['grade'] = grade
            student['status'] = 'GRADED'
def add_student(students, email, first_name, last_name, points):
    if email in students:
        print('Student juz istnieje')
    else:
        students[email] = {'first_name': first_name, 'last_name': last_name, 'points': points, 'grade': '', 'status': ''}

def remove_student(students, email):
    if email in students:
        del students[email]
    else:
        print('Student z tym email nie istnieje')

def send_emails(students):
    for email, student in students.items():
        if student['status'] != 'MAILED':
            print(f'Wysylam email:  {email} z punktami:  {student["grade"]}')
            student['status'] = 'MAILED'
if __name__ == '__main__':
    file_name = 'students.txt'
    students = read_data(file_name)
    grades(students)
    add_student(students, 'test@gmail,com', 'Jan', 'Kowalski', 85)
    remove_student(students, 'test@gmail.com')
    send_emails(students)