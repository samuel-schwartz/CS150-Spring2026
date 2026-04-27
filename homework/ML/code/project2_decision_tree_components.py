
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

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
reshaped_hw_and_quiz_scores = [[x1, x2] for (x1, x2) in zip(hw_scores, quiz_scores)]
model.fit(y=letter_grades, X=reshaped_hw_and_quiz_scores)
print("AI's predicted letter_grade", model.predict([[97,87]]))

# Plot Tree
# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree
# plot_tree(model, feature_names=["HW", "Quiz"], class_names=["A", "B", "C", "D", "F"], proportion=False, impurity=False)
# plt.show()


# Plot
import matplotlib.pyplot as plt
plt.close()
plt.scatter(hw_scores, quiz_scores, c=colors)
plt.xlabel('HW')
plt.ylabel('Quiz')

theoretical_hw_values = []
theoretical_quiz_values = []
predicted_grade_colors = []
for hw_value in range(1, 100):
    for qz_value in range(1, 100):
        theoretical_hw_values.append(hw_value)
        theoretical_quiz_values.append(qz_value)
        grade = model.predict([[hw_value, qz_value]])

        if grade == "A":
            pred_grade_color = "green"
        elif grade == "B":
            pred_grade_color = "orange"
        elif grade == "C":
            pred_grade_color = "blue"
        elif grade == "D":
            pred_grade_color = "purple"
        elif grade == "F":
            pred_grade_color = "red"
        else:
            pred_grade_color = "black"
        
        predicted_grade_colors.append(pred_grade_color)

plt.scatter(theoretical_hw_values, theoretical_quiz_values, c=predicted_grade_colors, s=0.25)

plt.show()
