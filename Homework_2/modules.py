def junior_student(object_students: list) -> None:
    #Вывести имя и возраст самого младшего студента.
    name, jun_student = object_students[0]["name"], object_students[0]["age"]

    for student in object_students[1:]:
        if student["age"] < jun_student:
            jun_student = student["age"]
            name = student["name"]
    print(f"Самый младший студент: {name}, возраст: {jun_student}")

def student_estimation_average(object_students: list) -> None:
    #Найти имя студента с самой высокой средней оценкой.
    max_average_grades = 0
    name = ''
    for student in object_students:
        average_grades_student = round((sum(student["grades"].values()) / len(student["grades"])), 2)
        if average_grades_student > max_average_grades:
            max_average_grades = average_grades_student
            name = student['name']


    print(f"Студент с самой высокой средней оценкой: {name}, средний балл: {max_average_grades:.2f}")


def subject_with_high_average_score(object_students: list) -> None:
    #Найти предмет, по которому самый высокий средний балл среди всех студентов.
    subjects = {}
    for student in object_students:
        for subject ,grade in student["grades"].items():
            if subject not in subjects:
                subjects[subject] = [grade, 1]
            else:
                subjects[subject][0] += grade
                subjects[subject][1] += 1

    max_grade = 0
    subject_name = ''
    for subject ,grades in subjects.items():
        avg_grade = round(grades[0] / grades[1], 2)
        if max_grade < avg_grade:
            max_grade = avg_grade
            subject_name = subject

    print(f"Предмет с самым высоким средним баллом: {subject_name}, средний балл: {max_grade:.2f}")

def students_with_average_score_3(object_students: list) -> dict:
    # Удалить всех студентов, чей средний балл ниже 3.0.
    students_with_average_score_3 = {}
    for student in object_students:
        average_grades_student = round((sum(student["grades"].values()) / len(student["grades"])), 2)
        if average_grades_student > 3:
            students_with_average_score_3[student["name"]] = average_grades_student

    return students_with_average_score_3

students = [
    {"name": "Иван", "age": 20, "grades": {"математика": 4, "физика": 5, "химия": 3}},
    {"name": "Мария", "age": 19, "grades": {"математика": 5, "физика": 5, "химия": 5}},
    {"name": "Пётр", "age": 21, "grades": {"математика": 3, "физика": 4, "химия": 2}},
    {"name": "Анна", "age": 22, "grades": {"математика": 5, "физика": 4, "химия": 4}},
]

# Вывести имя и возраст самого младшего студента.
junior_student(students)
# Найти имя студента с самой высокой средней оценкой.
student_estimation_average(students)
# Найти предмет, по которому самый высокий средний балл среди всех студентов.
subject_with_high_average_score(students)
# Удалить всех студентов, чей средний балл ниже 3.0.
print("Студенты с баллом выше 3.0:")
for name, avg_grade in students_with_average_score_3(students).items():
    print(f"{name}: средний балл = {avg_grade:.2f}")