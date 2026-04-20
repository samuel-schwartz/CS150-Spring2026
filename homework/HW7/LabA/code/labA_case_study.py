"""
This module contains classes which assign student grades in different locales.
"""
# Import Statements Here
import math


# Classes Start Here
class ChileanGradeAssigner:
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
        """
        This method calculates the final score of a student based on the weights provided.
        :param homework_score: The score of a student on all homework. Usually ranges from 0 to 100.
        :param quizzes_score: The score of a student on all quizzes. Usually ranges from 0 to 100.
        :param exams_score: The score of a student on all exams. Usually ranges from 0 to 100.
        :return: The final score of a student, usually ranging from 0 to 100.
        """
        final_score = 0
        final_score += self.homework_weight * homework_score
        final_score += self.quizzes_weight * quizzes_score
        final_score += self.exams_weight * exams_score
        final_score = math.ceil(final_score)
        return final_score

    @staticmethod
    def get_final_grade(final_score):
        """
        This method determines the grade a student earned.
        :param final_score: The numeric score a student earned in the class.
        :return: A grade in string form.
        """
        if final_score >= 85:
            return "Seven"
        elif final_score >= 70:
            return "Six"
        elif final_score >= 55:
            return "Five"
        elif final_score >= 40:
            return "Four"
        elif final_score >= 30:
            return "Three"
        elif final_score >= 15:
            return "Two"
        else:
            return "One"

    def print_student_grades(self, students_table):
        """
        This method prints student grades to the console.
        :param students_table: A list of lists, containing student information.
        :return: Nothing.
        """
        self.print_header()
        for row in students_table:
            student_name = row[0]
            hw_score = row[1]
            quizzes_score = row[2]
            exams_score = row[3]

            final_score = self.get_final_score(hw_score, quizzes_score, exams_score)
            final_grade = self.get_final_grade(final_score)
            print(student_name, final_score, final_grade, sep="\t")

    def print_header(self):
        """
        Prints the header requested to the console.
        :return: Nothing.
        """
        print("Final Grades")
        print("Weights: ",
              "Homework at ", self.homework_weight,
              "; Quizzes at ", self.quizzes_weight,
              "; Exams at ", self.exams_weight, ";",
              sep="")
        print()
        print("Name", "%", "Grade", sep="\t")


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


ChileanGradeAssigner(0.25, 0.20, 0.55).print_student_grades(STUDENTS)

print()

ChileanGradeAssigner(0.60, 0.20, 0.20).print_student_grades(STUDENTS)
