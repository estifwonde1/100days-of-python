print("welcome to the treasure map")
line_1 = [" "," "," "]
line_2 = [" "," "," "]
line_3 = [" "," "," "]

map = [line_1,line_2,line_3]
print("hiding ur treasure map , X marks the spot")
position=input().lower()
letter = position[0]
abd = ['a','b','c']
letters_index = abd.index(letter)




map[int(row)][int(column)] = "X"

print(f"{line_1}\n{line_2}\n{line_3}")