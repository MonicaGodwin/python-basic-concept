students = (
    ("Monica", 22, "Python", 85),
    ("John", 25, "Go", 72),
    ("Lucy", 21, "Java", 91),
    ("David", 24, "Python", 65)
)
count = 0
highest = 0
student_name = ""
for student in students:
    name,age,course,score = student
    if score >= 70:
        print(f"{name} - passed")
    else:
        print(f"{name} - Failed")
   
    if course == "Python":
        count += 1
print(f"Python Student: {count}")

for student in students:
    name,age,course,score = student
    if score > highest:
        highest = score
        student_name = name
print(f"Highest_Score: {student_name} - {highest}")

