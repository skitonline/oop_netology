class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        finished_courses_str = ', '.join(self.finished_courses)
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {avg_grade(self.grades)}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
               f'Завершенные курсы: {finished_courses_str}'

    def __lt__(self, student):
        return avg_grade(self.grades) < avg_grade(student.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg_grade(self.grades)}'

    def __lt__(self, lecturer):
        return avg_grade(self.grades) < avg_grade(lecturer.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            print(student.grades)
        else:
            print('Ошибка')


def avg_grade(grades):
    amount = 0
    count = 0
    for grades in grades.values():
        amount += sum(grades, 0)
        count += len(grades)
    return 'нет оценок' if count == 0 else amount / count


def avg_grade_for_course_student(students, course):
    amount = 0
    count = 0
    for student in students:
        grades = student.grades.get(course, [])
        amount += sum(grades, 0)
        count += len(grades)
    return 'нет оценок' if count == 0 else amount / count


def avg_grade_for_course_lecturer(lecturers, course):
    return avg_grade_for_course_student(lecturers, course)


student_1 = Student('Student_1', 'Surname', 'your_gender')
student_1.courses_in_progress += ['js', 'c++']
student_1.finished_courses += ['python', 'ruby']
student_1.grades['python'] = [10, 6, 5]
student_1.grades['js'] = [5, 5]
print(student_1)
print()

student_2 = Student('Student_2', 'Surname', 'your_gender')
student_2.courses_in_progress += ['python', 'ruby', 'go']
student_2.finished_courses += ['js', 'c++']
student_2.grades['python'] = [9]
print(student_2)
print()

print(student_1 < student_2)
print(student_1 > student_2)
print()

lecturer_1 = Lecturer('Lecturer_1', 'Surname')
lecturer_1.courses_attached = ['python']
lecturer_1.grades['python'] = [10, 10, 9]
print(lecturer_1)
print()

lecturer_2 = Lecturer('Lecturer_2', 'Surname')
lecturer_2.courses_attached = ['python', 'ruby', 'go']
lecturer_2.grades['python'] = [10, 10, 10]
lecturer_2.grades['ruby'] = [10, 6]
print(lecturer_2)
print()

print(lecturer_1 < lecturer_2)
print(lecturer_1 > lecturer_2)
print()

reviewer_1 = Reviewer('Reviewer_1', 'Surname')
print(reviewer_1)
print()

reviewer_2 = Reviewer('Reviewer_2', 'Surname')
print(reviewer_2)
print()

print(lecturer_1.grades)
student_2.rate_hw(lecturer_1, 'python', 1)
print(lecturer_1.grades)
print()

print(lecturer_2.grades)
student_2.rate_hw(lecturer_2, 'go', 1)
print(lecturer_2.grades)
print()

#несуществующий курс
student_1.rate_hw(lecturer_2, 'js++', 5)
#не лектор
student_2.rate_hw(reviewer_1, 'python', 5)
print()

print(avg_grade_for_course_student([student_1, student_2], 'python'))
print(avg_grade_for_course_student([student_1, student_2], 'js'))
#несуществующий предмет
print(avg_grade_for_course_student([student_1, student_2], 'js++'))
print()

print(avg_grade_for_course_lecturer([lecturer_1, lecturer_2], 'ruby'))
