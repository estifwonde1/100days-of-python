print("welcome to the treasure map")
line_1 = [" "," "," "]
line_2 = [" "," "," "]
line_3 = [" "," "," "]

map = [line_1,line_2,line_3]
print("hiding ur treasure map , X marks the spot")
position=input("enter the ").lower()
letter = ["a","b","c"]
row = po
column = row.len()-1

map[int(row)][int(column)] = "X"

print(f"{line_1}\n{line_2}\n{line_3}")