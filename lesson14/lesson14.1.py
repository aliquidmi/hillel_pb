from typing import Optional


class TooManyStudentsError(Exception):
    """Користувацький виняток для перевищення кількості студентів у групі."""
    def __init__(self, message: str = "У групі не може бути більше 10 студентів") -> None:
        super().__init__(message)


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}, Record Book: {self.record_book}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.record_book == other.record_book

    def __hash__(self) -> int:
        return hash(self.record_book)


class Group:
    def __init__(self, number: str) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise TooManyStudentsError()
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        if not self.group:
            return f"Group {self.number} is empty"
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group {self.number}:\n{all_students}"

if __name__ == "__main__":
    group = Group("PD1")

    try:
        for i in range(11):
            student = Student("Male", 20 + i, f"Name{i}", f"Surname{i}", f"AN14{i}")
            group.add_student(student)

    except TooManyStudentsError as e:
        print(f"Виняток: {e}")

    print("\nПоточний склад групи:")
    print(group)

    print("\nПошук:")
    print(group.find_student("Surname0"))
    print(group.find_student("NotExist"))

    print("\nВидалення:")
    group.delete_student("Surname0")
    print(group)

    group.delete_student("Surname0")
