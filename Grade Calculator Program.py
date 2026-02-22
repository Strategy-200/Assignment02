# Grade Calculator Program
# This program calculates total, percentage, grade, and pass/fail result

# Taking marks input for 5 subjects
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))
subject4 = int(input("Enter marks for Subject 4: "))
subject5 = int(input("Enter marks for Subject 5: "))

# Calculating total and percentage
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

# Determining grade
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Determining pass/fail result (each subject >= 40)
if subject1 >= 40 and subject2 >= 40 and subject3 >= 40 and subject4 >= 40 and subject5 >= 40:
    result = "Pass"
else:
    result = "Fail"

# Displaying results
print("\n=== RESULT ===")
print("Marks:")
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Subject 4:", subject4)
print("Subject 5:", subject5)

print("\nTotal Marks:", total_marks, "/ 500")
print("Percentage:", f"{percentage:.2f}%")
print("Grade:", grade)
print("Result:", result)