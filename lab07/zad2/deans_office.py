from student import Student
from exceptions import StudentCurrentlyExistsException
from exceptions import StudentNotExistsException


class DeansOffice:
    def __init__(self):
        self.list = []

    def add_student(self, student: Student):
        try:
            if student not in self.list:
                self.list.append(student)
            else:
                raise StudentCurrentlyExistsException(student)
        except StudentCurrentlyExistsException as error:
            print(f"Error occured: {error}")

    def remove_student(self, student_id):
        try:
            for student in self.list:
                if student.get_id() == student_id:
                    self.list.remove(student)
                    break
            else:
                raise StudentNotExistsException(student_id)
        except StudentNotExistsException as error:
            print(f"Error occured: {error}")

    def __repr__(self):
        cls = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"(({cls}): {attrs})"
