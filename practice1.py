# Program to accept marks of 5 subjects and evaluate grade

marks = []   # list to store subject marks

# Accepting marks for 5 subjects
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)

# Calculate total and average
total = sum(marks)
average = total / 5

# Grade evaluation based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Output
print("hello")
print("\n--- Result ---")
print("student marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)