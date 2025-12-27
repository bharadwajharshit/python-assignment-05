# Create a dictionary of student names and their marks
student_marks = {
    "Amit": 85,
    "Neha": 92,
    "Rahul": 78,
    "Priya": 88
}

# Ask the user to input a student's name
name = input("Enter the student's name: ")

# Retrieve and display the marks
if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found in the records.")
