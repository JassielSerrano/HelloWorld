# keep track of students in a class
# student's name
# age
# gather all student's names
# count how many students in class
student_1 = {"age": 18, "name": "George"}
student_2 = {"age": 17, "name": "Matt"}

lesson_1_students = [student_1, student_2]

lesson_1 = {"name": "data structures",
            "students": lesson_1_students}

def number_of_students(lesson):
    return len(lesson['students'])

# iteration using for loops in python
def student_names(lesson):
    for student in lesson['students']:
        print(student['name'])