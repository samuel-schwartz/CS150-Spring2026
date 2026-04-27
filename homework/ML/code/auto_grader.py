"""
This module contains a class to facilitate grading of code.
"""
import math
import sys
from pylint.lint import Run


class AutoGrader:
    """
    This class auto-grades a .py file on:
     (1) Formatting/Readability based on Pylint.
    """

    def __init__(self, code_file_name):
        self._code_file_name = code_file_name

    def _process_readability_score(self):
        print("PYLINT output will appear here:")
        results = Run(['--disable=R0901,R0902,R0903,R1705', self._code_file_name], do_exit=False)
        return math.ceil(results.linter.stats['global_note'])

    def get_arguments(self):
        """
        This method gets the arguments used in processing the code.
        :return: code file name, ideal output filename
        """
        return self._code_file_name

    def print_sub_total(self):
        """
        This method prints the validity and readability score based
        on the arguments passed to the constructor.
        :return: Nothing.
        """
        readability_score = self._process_readability_score()

        print("File being scored:", self._code_file_name)
        print("Validity Score will be determined by a human running your code.")
        print("Readability Score:", readability_score)

PY_FILE_NAME_TO_GRADE = sys.argv[1]

try:
    IDEAL_OUTPUT_FILE_NAME = sys.argv[2]
except IndexError:
    IDEAL_OUTPUT_FILE_NAME = None

AutoGrader(PY_FILE_NAME_TO_GRADE).print_sub_total()
