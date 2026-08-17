print("let's find out who has the hight score")
scores = input().split()
high = 0
for n in range(0,len(scores)):
    if high < int(scores[n]):
        high = int(scores[n])
print(high)
