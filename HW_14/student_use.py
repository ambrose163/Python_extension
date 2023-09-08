"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения
с выводом подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник
со сторонами отрицательной длины.
"""
from student_exeptions import StudentNameError, InvalidScoreError, InvalidSubjectError
from student import Student

try:
    student = Student("Дмитрий Иванов", "ivanov.csv")
    student.add_score("math", 5)
    student.add_test_result("math", 94)
    print(student.average_test_score("math"))
    print(student.average_score())

except InvalidSubjectError as e:
    print("Error:", e)

except StudentNameError as e:
    print("Error:", e)

except InvalidScoreError as e:
    print("Error:", e)
