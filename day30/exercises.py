# fruits = eval(input())

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruits Pie")
#     else:
#         print(fruit + "Pie")


# make_pie(4)

facebook_posts=eval(input())
total_likes = 0

for post in facebook_posts:
    try:
        total_likes  = total_likes + post['Likes']
    except KeyError:
        pass
   
print(total_likes)