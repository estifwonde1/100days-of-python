print("let's ur grade")
scores = {
    "Harry": 81,
    "Ron": 78,
    "Herminone":99,
    "Draco": 74,
    "Nevile":62,
}
stu ={}
for key in scores:
    if scores[key] >= 91:
        stu[key] = "Outstanding"
    elif scores[key] >= 81:
        stu[key] = "Exceeds expectation"
    elif scores[key] >= 71:
        stu[key] = "Acceptable"
    else:
        stu[key] = "Fail"
print(stu)