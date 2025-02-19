from modules import (junior_student, student_estimation_average,
                     subject_with_high_average_score, students_with_average_score_3)

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
