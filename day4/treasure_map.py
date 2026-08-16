print("welcome to the treasure map")
line_1 = [" "," "," "]
line_2 = [" "," "," "]
line_3 = [" "," "," "]

map = [line_1,line_2,line_3]
print("hiding ur treasure map , X marks the spot")
position=input().lower()
letter = position[0]
abd = ['a','b','c']
letter_index = abd.index(letter)
num_index = int(position[1]) -1



map[int(letter_index)][int(num_index)] = "X"

print(f"{line_1}\n{line_2}\n{line_3}")