
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

# Linear regression
from sklearn.linear_model import LinearRegression

# y = mX + b
# Linear regression for predicting exam score given quiz score

model = LinearRegression()
reshaped_exam_scores = [[y] for y in exam_scores]
reshaped_quiz_scores = [[x] for x in quiz_scores]
model.fit(y=reshaped_exam_scores, X=reshaped_quiz_scores)
print("m and b", model.coef_, model.intercept_)
print("AI's predicted exam score", model.predict([[87]]))

# Plot it
plt.scatter(quiz_scores, exam_scores, c=colors)
plt.xlabel('Quiz')
plt.ylabel('Exam')

theoretical_quiz_values = []
predicted_exam_values = []
for value in range(1, 100):
    theoretical_quiz_values.append(value)
    pev = model.coef_[0] * value + model.intercept_
    predicted_exam_values.append(pev)

plt.scatter(theoretical_quiz_values, predicted_exam_values, s=0.5, c="gray")

plt.show()

# Linear regression for predicting exam score given HW score
model = LinearRegression()
reshaped_exam_scores = [[y] for y in exam_scores]
reshaped_hw_scores = [[x] for x in hw_scores]
model.fit(y=reshaped_exam_scores, X=reshaped_hw_scores)

print("m and b", model.coef_, model.intercept_)
print("AI's predicted exam score", model.predict([[97]]))

# Plot it
# plt.clf()
# plt.scatter(hw_scores, exam_scores, c=colors)
# plt.xlabel('HW')
# plt.ylabel('Exam')

# theoretical_quiz_values = []
# predicted_exam_values = []
# for value in range(1, 100):
#     theoretical_quiz_values.append(value)
#     pev = model.coef_[0] * value + model.intercept_
#     predicted_exam_values.append(pev)

# plt.scatter(theoretical_quiz_values, predicted_exam_values, s=0.5, c="gray")

#plt.show()



# Linear regression for predicting exam score given HW score and quiz score
# y = m1*hw_score + m2*quiz_score + b
model = LinearRegression()
reshaped_exam_scores = [[y] for y in exam_scores]
reshaped_hw_and_quiz_scores = [[x1, x2] for (x1, x2) in zip(hw_scores, quiz_scores)]
model.fit(y=reshaped_exam_scores, X=reshaped_hw_and_quiz_scores)

print("m1, m2, and b", model.coef_, model.intercept_)
print("AI's predicted exam score", model.predict([[97,87]]))

# Plot it
plt.close()
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(hw_scores, quiz_scores, exam_scores, c=colors)

theoretical_hw_values = []
theoretical_quiz_values = []
predicted_exam_values = []
for hw_value in range(80, 100):
    for qz_value in range(80, 100):
        theoretical_hw_values.append(hw_value)
        theoretical_quiz_values.append(qz_value)
        pev = model.coef_[0][0] * hw_value + model.coef_[0][1] * qz_value + model.intercept_[0]
        pred = model.predict([[hw_value, qz_value]])
        print("Manually Calculated", pev, "Auto Pred", pred)
        predicted_exam_values.append(pev)

ax.scatter(theoretical_hw_values, theoretical_quiz_values, predicted_exam_values, s=0.5, c="gray")

ax.set_xlabel('HW')
ax.set_ylabel('Quiz')
ax.set_zlabel('Exam')

plt.show()