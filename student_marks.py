name = "Goutham"
marks = [85, 90, 78, 92, 88]

average = sum(marks) / len(marks)

print("Student:", name)
print("Marks:", marks)
print("Average:", average)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)
print("Processed by Developer B")