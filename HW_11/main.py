from student import Student

if __name__ == '__main__':
    student = Student('Dmitriy', 'Alexandrovich', 'Filatov', 'filatov.csv')
    # student = Student('Dmitriy', 'alexandrovich', 'Filatov', 'filatov.csv') # строчная буква
    # student = Student('Dmitry', 'Alexandrovich', 'F1latov', 'filatov.csv') # цифра в имени

    student.add_test_score("math", 63)
    student.add_test_score("math", 93)
    student.add_grade("math", 4)

    student.add_test_score("rus_lang", 82)
    student.add_test_score("rus_lang", 50)
    student.add_test_score("rus_lang", 84)
    student.add_grade("rus_lang", 4)

    student.add_test_score("physics", 94)
    student.add_grade("physics", 5)

    print(f'Средний бал тестов по математике: {student.average_test_score("math"):.1f}')
    print(f'Средний бал тестов по русскому языку: {student.average_test_score("rus_lang"):.1f}')
    print(f'Средний бал тестов по физике: {student.average_test_score("physics"):.1f}')
    print(f'Средняя оценка по всем предметам: {student.average_grade():.1f}')