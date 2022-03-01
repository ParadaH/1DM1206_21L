from exceptions import InvalidStudentParamsException


class Student:

    def __init__(self, name, surname, age, id_number):
        self.__checking_parameters(name, surname, age, id_number)
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__id_number = id_number

    def get_id(self):
        return self.__id_number

    def __checking_parameters(self, name, surname, age, id_number):
        if not isinstance(name, str) or len(name) < 1:
            raise InvalidStudentParamsException("name", name)

        if not isinstance(surname, str) or len(surname) < 1:
            raise InvalidStudentParamsException("surname", surname)

        if not isinstance(age, int) or age < 1 or age > 75:
            raise InvalidStudentParamsException("age", age)

        if not isinstance(id_number, int) or id_number < 1:
            raise InvalidStudentParamsException("id_number", id_number)

    def __repr__(self):
        cls = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"(({cls}): {attrs})"
