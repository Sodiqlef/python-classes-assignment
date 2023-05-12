class Assignment:
    def __init__(self, name: str, difficulty: float):
        self.__name = name
        self.__difficulty = difficulty

    def get_name(self) -> str:
        return self.__name

    def get_difficulty(self) -> float:
        return self.__difficulty

    def __str__(self) -> str:
        return self.__name


class AssignmentResult:
    def __init__(self, id: int, assignment: Assignment, grade: float):
        self.__id = id
        self.__assignment = assignment
        self.__grade = grade

    def get_id(self) -> int:
        return self.__id

    def get_grade(self) -> float:
        return self.__grade

    def get_assignment(self) -> Assignment:
        return self.__assignment


class Student:
    def __init__(self, id: int, first_name: str, last_name: str, town: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.town = town
        self.grades = []
        self.energy = 1.0

    def get_id(self) -> int:
        return self.id

    def get_first_name(self) -> str:
        return self.first_name

    def set_first_name(self, name: str):
        self.first_name = name

    def get_last_name(self) -> str:
        return self.last_name

    def set_last_name(self, name: str):
        self.last_name = name

    def get_town(self) -> str:
        return self.town

    def set_town(self, town: str):
        self.town = town

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_grade(self) -> float:
        if len(self.grades) == 0:
            return 0.0
        elif len(self.grades) == 1:
            return self.grades[0]
        else:
            return (sum(self.grades) - min(self.grades)) / (len(self.grades) - 1)

    def assign(self, assignment: Assignment) -> AssignmentResult:
        grade = 1.0 - (self.energy * assignment.difficulty)
        grade = max(0.0, grade)
        self.energy -= assignment.difficulty * self.energy
        self.energy = max(0.0, self.energy)
        self.grades.append(grade)
        return AssignmentResult(self.id, assignment, grade)

    def sleep(self, hours: float):
        self.energy += 0.1 * hours
        self.energy = min(1.0, self.energy)

    def get_energy(self):
        return self.energy


class Course:
    def __init__(self, students):
        self.students = students

    def get_mean_grade(self):
        total_grades = sum([student.get_grade() for student in self.students])
        return total_grades / len(self.students)

    def get_max_grade(self):
        return max([student.get_grade() for student in self.students])

    def get_min_grade(self):
        return min([student.get_grade() for student in self.students])

    def get_median_grade(self):
        sorted_grades = sorted([student.get_grade()
                               for student in self.students])
        num_students = len(self.students)
        mid = num_students // 2
        if num_students % 2 == 0:
            return (sorted_grades[mid - 1] + sorted_grades[mid]) / 2
        else:
            return sorted_grades[mid]

    def get_grade_variance(self):
        num_students = len(self.students)
        mean_grade = self.get_mean_grade()
        variance = sum([(student.get_grade() - mean_grade) **
                       2 for student in self.students]) / (num_students - 1)
        return variance

    def grade_std_dev(self):
        return self.get_grade_variance() ** 0.5

    def assign(self, name, difficulty):
        new_assignment = Assignment(name, difficulty)
        for student in self.students:
            student.assign(new_assignment)
