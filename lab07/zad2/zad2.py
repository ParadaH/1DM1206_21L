from lab07.zad2.deans_office import DeansOffice
from student import Student

if __name__ == "__main__":
    stud_1 = Student("Mikolaj", "Rej", 55, 123321)
    stud_2 = Student("Hubert", "Parada", 13, 433334)
    stud_3 = Student("Mariusz", "Pudzianowski", 56, 411231)
    stud_4 = Student("Mark", "McMorris", 28, 311234)
    stud_5 = Student("Craig", "McMorris", 31, 123123)
    stud_6 = Student("Hubert", "Parada", 31, 132312)

    students = DeansOffice()

    students.add_student(stud_1)
    students.add_student(stud_2)
    students.add_student(stud_3)
    students.add_student(stud_4)
    students.add_student(stud_5)
    students.add_student(stud_6)

    #tutaj dodaje studenta, ktory nalezy juz do listy
    students.add_student(stud_1)

    students.remove_student(123321)
    students.remove_student(433334)
    students.remove_student(411231)

    #tutaj usuwam studenta, ktory został usuniety juz wczesniej oraz probuje usunac studenta, ktory nie istnieje
    students.remove_student(123321)
    students.remove_student(111111)

    print(students)


