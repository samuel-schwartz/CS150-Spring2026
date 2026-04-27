
def etl_classwork_data(filename="grades_data.csv"):
    # Extract
    raw_data = []
    with open(filename, "r") as f:
        f.readline()  # Reads first line, the header
        for line in f:
            raw_data.append(line.split(","))

    # Transform
    student_names = []
    hw_scores = []
    quiz_scores = []
    exam_scores = []
    letter_grades = []

    for row in raw_data:
        student_names.append(row[0])
        hw_scores.append(float(row[1]))
        quiz_scores.append(float(row[2]))
        exam_scores.append(float(row[3]))
        letter_grades.append(row[4].strip())
    
    # Load
    return (student_names, hw_scores, quiz_scores, exam_scores, letter_grades)

# MatPlotLib
import matplotlib.pyplot as plt

# Load data, calculate colors

(student_names, hw_scores, quiz_scores, exam_scores, letter_grades) = etl_classwork_data()
colors = []

for grade in letter_grades:
    if grade == "A":
        colors.append("green")
    elif grade == "B":
        colors.append("orange")
    elif grade == "C":
        colors.append("blue")
    elif grade == "D":
        colors.append("purple")
    elif grade == "F":
        colors.append("red")
    else:
        colors.append("black")

# 2D

# plt.scatter(quiz_scores, exam_scores)
# plt.xlabel('Quiz')
# plt.ylabel('Exam')
#plt.show()

# plt.scatter(quiz_scores, exam_scores, c=colors)
# plt.xlabel('Quiz')
# plt.ylabel('Exam')
#plt.show()


# plt.scatter(hw_scores, exam_scores, c=colors)
# plt.xlabel('HW')
# plt.ylabel('Exam')
#plt.show()


plt.scatter(hw_scores, quiz_scores, c=colors)
plt.xlabel('HW')
plt.ylabel('Quiz')
plt.show()


# plt.scatter(hw_scores, quiz_scores, c=colors)
# plt.scatter([97], [87], c=["black"])
# plt.xlabel('HW')
# plt.ylabel('Quiz')
#plt.show()

#3D
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(hw_scores, quiz_scores, exam_scores, c=colors)
# ax.set_xlabel('HW')
# ax.set_ylabel('Quiz')
# ax.set_zlabel('Exam')
# plt.show()

