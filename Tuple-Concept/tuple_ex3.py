# Unpacking a tuple

student = ("Monica", 22, "Python")
name, age, course = student
print(name)
print(age)
print(course)


# Unpacking tuple inside a loop
students = (
    ("Monica", 22, "Python"),
    ("John", 25, "Go"),
    ("Lucy", 21, "Java")
)

for name, age, course in students:
    print(f"{name} is {age} years old and studies {course}")

# OR

for student in students:
    name, age, course = student
    print(f"{name} is {age} years old and studies {course}")

