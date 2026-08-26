from game_data import data
import art
import random
print(art.logo)
is_gameover = False
while not is_gameover:
    num = len(data)
    indie = random.randint(0,num-1)
    boomy = random.randint(0,num-1)
    if indie == boomy:
        continue
    higher = data[indie]
    needed_data = ["name","follower_count"]
    values = [higher[k] for k in needed_data]
    print(values[0])
    print(art.vs)
    lower = data[boomy]
    lower_needed_data = ["name","follower_count"]
    lower_value = [lower[k] for k in lower_needed_data]
    print(lower_value[0])


    break