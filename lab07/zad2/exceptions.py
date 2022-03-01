class InvalidStudentParamsException(Exception):
    def __init__(self, arg, result):
        msg = f"Invalid parameter: ({arg}): {result})"
        super().__init__(msg)


class StudentNotExistsException(Exception):
    def __init__(self, arg):
        msg = f"Student doesn't belong to Dean's Office (student: {arg})"
        super().__init__(msg)


class StudentCurrentlyExistsException(Exception):
    def __init__(self, arg):
        msg = f"Student already belongs to Dean's Office! {arg}"
        super().__init__(msg)
