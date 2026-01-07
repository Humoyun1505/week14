names = ["Alice", "Bob", "Charlie", "David", "Eve"]
gpas = [3.9, 3.2, 3.6, 3.7, 3.5]
hours = [10, 100, 60, 20, 40]

students = list(zip(names, gpas, hours))
eligible = [
    (name, gpa, h)
    for name, gpa, h in students
    if gpa >= 3.8 or (gpa >= 3.5 and h > 50)
]
eligible.sort(key=lambda x: (-x[1], -x[2]))
result = [f"{name}: {gpa} / {h}h" for name, gpa, h in eligible]

print(result)
