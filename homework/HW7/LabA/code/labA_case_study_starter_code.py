"""
This module implements a Chilean-style gradebook.
"""
# Import Statements Here
import math

# Classes Start Here
class ChileanGradeAssigner:
    """
    This class articulates Chilean-style grades based on weights and scores provided.
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
        """
        This method calculates the final score of a student based on the weights provided.
        :param homework_score: The score of a student on all homework. Usually ranges from 0 to 100.
        :param quizzes_score: The score of a student on all quizzes. Usually ranges from 0 to 100.
        :param exams_score: The score of a student on all exams. Usually ranges from 0 to 100.
        :return: The final score of a student, usually ranging from 0 to 100.
        """
        pass

    @staticmethod
    def get_final_grade(final_score):
        """
        This method determines the grade a student earned.
        :param final_score: The numeric score a student earned in the class.
        :return: A grade in string form.
        """
        pass

    def print_student_grades(self, students_table):
        """
        This method prints student grades to the console.
        :param students_table: A list of lists, containing student information.
        :return: Nothing.
        """

        #for index, my_list in enumerate(students_table):
        #    print(index, my_list)

        for (name, hw, qiz, ex) in students_table:
            name = row[0]
            value_as_str = str(hw+quiz+exam)
            print(index, name + "\t" + value_as_str)



    def print_header(self):
        """
        Prints the header requested to the console.
        :return: Nothing.
        """
        pass


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

gradebook = ChileanGradeAssigner(0.60, 0.20, 0.20)
gradebook.print_student_grades(STUDENTS)

