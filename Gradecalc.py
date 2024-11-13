# The student enters their score from test
Test1 = int(input("Please enter your first test score: "))
Test2 = int(input("Please enter your second test score: "))
Test3 = int(input("Please enter your third test score: "))

# Store grades in a list
grades = [Test1, Test2, Test3]

# Calculate the total score
total = sum(grades)

# Calculate the average (final score)
average = total / len(grades)

# Determine the grade based on the average score
#used some of my old middle school testing scores
if 96 <= average <= 100:
    grade = "A+"
elif 92 <= average < 96:
    grade = "A"
elif 90 <= average < 92:
    grade = "A-"
elif 86 <= average < 90:
    grade = "B+"
elif 82 <= average < 86:
    grade = "B"
elif 80 <= average < 82:
    grade = "B-"
elif 76 <= average < 80:
    grade = "C+"
elif 72 <= average < 76:
    grade = "C"
elif 70 <= average < 72:
    grade = "C-"
elif 66 <= average < 70:
    grade = "D+"
elif 62 <= average < 66:
    grade = "D"
elif 60 <= average < 62:
    grade = "D-"
else:
    grade = "F"

# Print the results
print("Scores:", grades)
print("Final Score:", average)
print("Grade:", grade)
