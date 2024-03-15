class Student:
    def __init__(self, name, number, list, grades):
        self.name = name
        self.number = number
        self_list = list
        self.grades = grades


def show_name(self):
    print(self.name)


def show_number(self):
    print(self.number)


def show_grades(self):
    print(self.grades)

def show_list(self):
    print(self.liat)





class Course:
    def __init__(self, named, teacher, list1):
        self.named = named
        self.teacher = teacher
        self_list1 = list1


def show_named(self):
    print(self.named)


def show_teacher(self):
    print(self.teacher)


def show_list1(self):
    print(self.list1)



class Teacher:
    def __init__(self, named1, courses, lists):
        self.named1 = named1
        self.courses = courses
        self_lists = lists




def show_named1(self):
    print(self.named1)


def show_courses(self):
    print(self.courses)


def show_lists(self):
    print(self.lists)


class School(Student, Teacher, Course):
    def __str__(self):
        return 'students' + Student.__init__(self) + 'teachers' + Teacher.__init__(self) + 'courses' + Course.__init__(self)


    student = Student('Lina', '44', '5555', '5')

    print(student)

    course = Course('First', '44', 'Elina')

    print(course)


    teacher = Teacher('Elina', 'First', 'Math')

    print(teacher)