print("Welcome to the love calculaltor where u can find love or not")
name = input("please enter ur name\n").lower()
another = input("please enter ur crush name\n").lower()
n =0
m = 0
if "t" in name:
    n += 1
if "r" in name:
    n +=1
if "u" in name:
     n +=1
if "e" in name:
    n +=1
if "l" in name:
    n += 1
if "o"in name:
    n +=1 
if "v" in name:
    n +=1
if "e" in name:
    n+=1
if "t" in another :
    m +=1 
if "r" in another:
    m += 1
if "u" in another:
    m += 1
if "e" in another:
    m +=1
if "l" in another:
    m +=1
if "o" in another:
    m += 1
if "v" in another:
    m += 1
if "e" in another:
    m += 1
score = str(n) + str(m)
if int(score) < 10 or int(score) > 90 :
    print(f"ur score got {score} u guys go like coke and mentos")
elif int(score) > 40 and int(score) < 50:
    print(f"ur score got {score} u are alright together") 
else:
    print(f"ur score got {score}")





