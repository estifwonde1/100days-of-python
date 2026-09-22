# numbers = [ 1,1,2,3,5,8,13,21,34,55]

# squared_numbers = [n**2 for n in numbers]
# print (squared_numbers)
# list_of_strings = input().split(",")

# string_to_num = [int(n) for n in list_of_strings]
# print(string_to_num)

# evens =[n for n in string_to_num if n % 2==0]
# print(evens)
# with open("file1.txt") as file1:
#     first=file1.readlines()
# with open("file2.txt") as file2:
#     second=file2.readlines()

# result =[int(n) for  n in first if n in second]
# print(result)
# sentence = input().split(" ")
# print(list(sentence))

# result = { letter : len(letter) for letter in list(sentence) }
# print(result)
# weather = eval(input())

# conver={value:conv*9/5 + 32 for value,conv in weather.items()}
# print(conver)
student_dict ={
    "student":["angela","james","lilly"],
    "grades":[56,76,98]
}
import pandas as pd

new_data=pd.DataFrame(student_dict)
new_data.to_csv("student_grades.csv")
loop ={key : value for (key,value) in new_data.iterrows()}