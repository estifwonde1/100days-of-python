print("let's ur grade")
scores = {
    "Harry": 81,
    "Ron": 78,
    "Herminone":99,
    "Draco": 74,
    "Nevile":62,
}
stu ={}
for key, score in scores.item():
    if scores >= 91:
        stu[key] = "Outstanding"
    elif scores >= 81:
        stu[key] = "Exceeds expectation"
    elif scores>= 71:
        stu[key] = "Acceptable"
    else:
        stu[key] = "Fail"
print(stu)