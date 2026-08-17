print("welcome to the average height calulator")
students_height = input().split()
sum = 0
for n in range (0, len(students_height)):
    students_height[n] =int(students_height[n])
    sum += students_height[n]
    le = len(students_height)
    av = sum/le
print(av)
    
