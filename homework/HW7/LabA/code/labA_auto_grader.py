"""
This module contains a class to facilitate grading of code.
"""
import math
import os
import subprocess
import sys
from pylint.lint import Run


class AutoGrader:
    """
    This class auto-grades an .py file on:
     (1) Formatting/Readability based on Pylint.
     (2) Validity as given by a model output.
    """

    def __init__(self, code_file_name, ideal_output_filename):
        self._code_file_name = code_file_name
        if ideal_output_filename is None:
            self._ideal_output_filename = "ideal_output.txt"
        else:
            self._ideal_output_filename = ideal_output_filename

    def _process_validity_score(self):
        subprocess.run(['bash -c "/home/student/anaconda3/bin/python3 ' +
                        self._code_file_name + ' > out.txt"'], shell=True)

        print("DIFF output (if any) will appear here:")
        subprocess.run(['sdiff -s out.txt ' + str(self._ideal_output_filename)], shell=True)

        diff_result = subprocess.run(['sdiff -s out.txt ' +
                                      str(self._ideal_output_filename) +
                                      ' | wc -l'], shell=True, stdout=subprocess.PIPE)

        diff_line_count = int(diff_result.stdout.decode('utf-8'))

        file_length = len(open(self._ideal_output_filename).readlines())

        os.remove("out.txt")

        score = (1-(diff_line_count/file_length))*10

        print("Your output's validity has been rated at: "+str(round(score, 2))+"/10")

        return math.ceil(score)

    def _process_readability_score(self):
        print("PYLINT output will appear here:")
        results = Run(['--disable=R0901,R0902,R0903,R1705', self._code_file_name], do_exit=False)
        return math.ceil(results.linter.stats['global_note'])

    def get_arguments(self):
        """
        This method gets the arguments used in processing the code.
        :return: code file name, ideal output filename
        """
        return self._code_file_name, self._ideal_output_filename

    def print_sub_total(self):
        """
        This method prints the validity and readability score based
        on the arguments passed to the constructor.
        :return: Nothing.
        """
        validity_score = self._process_validity_score()
        readability_score = self._process_readability_score()

        print("File being scored:", self._code_file_name)
        print("Validity Score:", validity_score)
        print("Readability Score:", readability_score)


PY_FILE_NAME_TO_GRADE = sys.argv[1]

try:
    IDEAL_OUTPUT_FILE_NAME = sys.argv[2]
except IndexError:
    IDEAL_OUTPUT_FILE_NAME = None

AutoGrader(PY_FILE_NAME_TO_GRADE, IDEAL_OUTPUT_FILE_NAME).print_sub_total()
