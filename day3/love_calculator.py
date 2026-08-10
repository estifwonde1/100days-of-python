print("Welcome to the love calculaltor where u can find love or not")
name = input("please enter ur name").lower()
another = input("please enter ur crush name").lower()
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

print (f"ur love number is {str(n) + str(m)}")



