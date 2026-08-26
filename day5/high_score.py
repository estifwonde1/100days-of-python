print("let's find out who has the hight score")
scores = input().split()
high = 0
for n in range(len(scores)):
    high = max(high, int(scores[n]))
print(high)
