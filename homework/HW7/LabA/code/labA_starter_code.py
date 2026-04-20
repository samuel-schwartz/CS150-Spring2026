"""
This module contains classes which assign student grades in different locales.
"""
# Import Statements Here
import math


# Classes Start Here
class USGradeAssigner:
    """
    This class articulates grades based on weights and scores provided.
    """
    # Constructor
    def __init__(self, homework_weight, quizzes_weight, exams_weight):
        """
        :param homework_weight: The weight homework will carry in the final score of a student.
        It's a floating value ranging between 0 and 1.
        :param quizzes_weight: The weight quizzes will carry in the final score of a student.
        It's a floating value ranging between 0 and 1.
        :param exams_weight: The weight exams will carry in the final score of a student.
        It's a floating value ranging between 0 and 1.
        """
        self.homework_weight = homework_weight
        self.quizzes_weight = quizzes_weight
        self.exams_weight = exams_weight

    # Methods
    def get_final_score(self, homework_score, quizzes_score, exams_score):
        # Write this method. Be sure to include documentation and remove the pass keyword when done.
        pass

    @staticmethod
    def get_final_grade(final_score):
        # Write this method. Be sure to include documentation and remove the pass keyword when done.
        pass

    def print_student_grades(self, students_table):
        # Write this method. Be sure to include documentation and remove the pass keyword when done.
        pass


# Class articulation has now ended. Below this line is where the execution of the program occurs.

# Student Data
STUDENTS = [
    ["Alexis", 80, 89, 92],
    ["Andrew", 87, 76, 74],
    ["Ashley", 98, 84, 88],
    ["Austin", 92, 93, 87],
    ["Brandon", 78, 75, 75],
    ["Chris", 97, 89, 89],
    ["Eliza", 100, 91, 72],
    ["Emily", 100, 95, 95],
    ["Hannah", 65, 90, 86],
    ["Jacob", 71, 76, 85],
    ["Jessica", 100, 90, 100],
    ["Joshua", 91, 91, 91],
    ["Madison", 13, 38, 38],
    ["Matthew", 88, 48, 68],
    ["Michael", 99, 94, 89],
    ["Nick", 73, 92, 84],
    ["Sammy", 94, 84, 71],
    ["Sarah", 33, 26, 37],
    ["Taylor", 93, 89, 90],
    ["Tyler", 96, 92, 93]
]


USGradeAssigner(0.25, 0.20, 0.55).print_student_grades(STUDENTS)

print()

USGradeAssigner(0.60, 0.20, 0.20).print_student_grades(STUDENTS)
