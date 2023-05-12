Classes
Please create a python module named homework.py and implement the classes and methods outlined below. Below you will find an explanation for each class and method you need to implement. When you are done please upload the file homework.py to Grader Than. Please get started as soon as possible on this assignment. This assignment has many problems, it may take you longer than normal to complete this assignment.

This assignment is supposed to represent a group of students in a course. A group of students in a course will be assigned an assignment and produce a collection of assignment results. The results will be used to figure out grade statistics. The grade they receive for their work on the assignment is entirely dependant on the student's energy level. If the student works on many assignments without sleeping their grade will suffer. You will implement four classes (Assignment, AssignmentResult, Student, and Course), they will depend on each other in the order they are listed. 

Hint:  Work on the methods in the order they are found in the documentation below, implement the getter and setter methods before the more complicated methods. Work on the Assignment class, AssignmentResult class, Student class and Course class in that order. 

Make sure you don't name your class variables the same name as you class's methods. In other words if you have method named id you cannot have a class variable named self.id. To avoid name conflicts often developers will start the name of their class variables with 2 underscores "". For example self._id = 123 

Class Assignment
This object represents a school assignment that a student will work on.

_init_(self, name: str, difficulty: float):
    """
    Constructs an assignment with the given assignment name and a float that indicates the level of difficulty of
    the assignment.
    :param name: The name of the assignment
    :param difficulty: The level of difficulty of the assignment
    """
get_name(self) -> str:
    """
    Returns the name of the assignment as specified in the constructor.
    :return: The assignment name
    """
get_difficulty(self) -> str:
    """
    Returns the level of difficulty of the assignment as specified in the constructor.
    :return: The assignment level
    """
_str_(self) -> str:
    """
    Returns the name of the assignment as specified in the constructor.
    :return: The assignment name
    """
Class AssignmentResult
An object that represents the result of an assignment.

_init_(self, id:int, assignment: Assignment, grade: float):
    """
    This will contain the ID of the student, the assignment
    that the student worked on and the grade the student received on the assignment.
    :param id: The ID of the student that created this Assignment result
    :param assignment: The Assignment that the student worked on.
    :param grade: A number between 0-1 representing the numerical grade the student received
    """
get_id(self) -> int:
    """
    Returns the ID of the student as specified in the constructor.
    :return: The student's ID
    """
get_grade(self) -> float:
    """
    Returns the grade as specified in the constructor.
    :return: The grade the student received for this assignment
    """
get_assignment(self) -> Assignment:
    """
    Returns the assignment as specified in the constructor.
    :return: The assignment that the student worked on to create this result
    """
Class Student
This class represents a single student

_init_(self, id: int, fist_name: str, last_name: str, town:str):
    """
    This creates a student object with the specified ID first and last name and home town. This constructor should
    also create data structure for holding the students grades for all of there assignments. Additionally it should
    create a variable that holds the student's energy level which will be a number between 0 and 1. The student start
    out with 1 (100%) energy.
    :param id: The student's identifiaction number
    :param fist_name: The student's first name
    :param last_name: The student's last name
    :param town: The student's home town
    """
get_id(self)->int:
    """
    Returns the ID of the student as specified in the constructor.
    :return: The student's ID
    """
get_first_name(self) -> str:
    """
    Returns the first name of the student.
    :return: The student's first name
    """
set_first_name(self, name:str):
    """
    Changes the student first name to the specified value of the name parameter.
    :param name: The value that the first name of the student will equal.
    """
get_last_name(self) -> str:
    """
    Returns the last name of the student.
    :return: The student's last name
    """
set_last_name(self, name: str):
    """
    Changes the student last name to the specified value of the name parameter.
    :param name: The value that the last name of the student will equal.
    """
get_town(self) -> str:
    """
    Returns the hometown of the student.
    :return: The student's town name
    """
set_town(self, town: str):
    """
    Changes the student's hometown to the specified value of the town parameter.
    :param name: The value that the hometown of the student will equal.
    """
_str_(self) ->str:
    """
    Returns a string containing the student's first and last name separated by a space.
    :return: Returns a string of the full name of the student
    """
get_grade(self)->float:
    """
    Calculates a an average grade based off of the student's past assignment's grades. The lowest grade is not
    included in the grade calculation if the student has been assigned to two or more assignments in the past.
    See assign() for more detains. If the student has not been assigned any assignments in the pass this should
    return 0.
    :return: A number between 0-1 indicating the student's grade
    """
assign(self, assignment:Assignment) -> AssignmentResult:
    """
    This function is to simulate the process of the student receiving an assignment, then working on the
    assignment, then submitting the assignment and finally receiving grade for the assignment. This function will
    receive an assignment then a grade should be calculated using the following formula:
    grade = 1 - (Student's current energy X Assignment difficulty level). The min grade a student may receive is 0% (0)

    After the grade is calculated the student's energy should be decreased by percentage difficulty.
    Example if the student has 80% (.8) energy and the assignment is a difficultly level .2 there final energy
    should be 64% (.64) = .8 - (.8 * .2). The min energy a student may have is 0% (0)

    Finally the grade calculated should be stored internally with in this class so it can be retrieved later.
    Then an Assignment Result object should be created with the student's ID, the assignment
    received as a parameter, and the grade calculated. This newly created Assignment Result object
    should be returned.

    :return: The an AssignmentResult outlining this process
    """
sleep(self, hours:float):
    """
    This function restore the student's energy as a rate of 10% per hour. So if they sleep for 8 hours there energy
    will be restored by 80%. If they have 50% (.5) energy and sleep for 8 hours the will wake up with 90% energy
    = (.5 * (1+.8)). The max energy a s student may have is 100% (1)
    :param hours: The number of hours a student will sleep for. Example: .2 is equal to 12 minutes or 20% of an hour.
    :return: None
    """
get_energy(self):
    """
    Returns the current energy of the student. A number between 0 and 1
    :return: The energy of the student.
    """
Class Course
This class represents a course that a group of students is enrolled in. They will be assigned assignments when enrolled in this course. This object will be used to calculate aggregate student statistics.

_init_(self, students: list):
    """
    Constructs a course with the specified list of students (student objects)
    :param students: A list containing one or more students
    """
get_mean_grade(self) -> float:
    """
    Returns the numerical value of the class mean (average) grade.
    :return: The average student grade
    """
get_max_grade(self) -> float:
    """
   Returns the highest grade in the class.

   The grades used in the calculation come from the student.grade(), it does not care if a grade was earned
    when the student was in another class.
   :return: The highest grade in the class
   """
get_min_grade(self):
    """
   Returns the lowest grade in the class.

   The grades used in the calculation come from the student.grade(), it does not care if a grade was earned
    when the student was in another class.
   :return: The lowest grade in the class
   """
get_median_grade(self) -> float:
    """
    Calculates and returns the median (middle value) of all the student's grades in this course

    The grades used in the calculation come from the student.grade(), it does not care if a grade was earned
    when the student was in another class.
    :return: The median grade
    """
get_grade_variance(self) -> float:

    """
    Calculates and returns the sample variance of all the student's grades in this course

    The grades used in the calculation come from the student.grade(), it does not care if a grade was earned
    when the student was in another class.
    :return: The sample variance of the grades
    """
grade_std_dev(self) -> float:

    """
    Calculates and returns the sample standard deviation of all the student's grades in this course.

    The grades used in the calculation come from the student.grade(), it does not care if a grade was earned
    when the student was in another class.
    :return: The sample standard deviation of the grades
    """
assign(self, name: str, difficulty: float) -> None:
    """
    This creates an assignment using the parameters specified, then assigns it to all of the students in this
    course, by calling the assign method on each student. Subsequent invocations to the statistics methods above
    should reflect the changes made by this method after it is called. In other words if a very difficult
    assignment is assigned the course mean should be less after.
    :param name: The name of the assignment
    :param difficulty: The level of difficulty of the assignment
    :return: None
    """
