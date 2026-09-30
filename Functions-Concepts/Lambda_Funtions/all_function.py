students = [
    ("Monica", 85),
    ("John", 72),
    ("Alex", 91),
    ("David", 65),
    ("Lucy", 88)
]

high_score = lambda scores: scores[1] > 80
result = list(filter(high_score, students))
print(result)

sort_student = sorted(result, key=lambda score: score[1], reverse=True)
print(sort_student)

mapped_student = lambda name: name[0]
result = list(map( mapped_student, sort_student))
print(result)