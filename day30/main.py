try:
    file = open("exception.txt")
    content = file.read()
except FileNotFoundError:
    file = open("exception.txt","w")
    file.write("someting")