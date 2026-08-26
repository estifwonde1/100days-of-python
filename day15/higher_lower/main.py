from game_data import data
import art
import random
print(art.logo)
is_gameover = False
while not is_gameover:
    num = len(data)
    indie = random.randint(0,num-1)
    boomy = random.randint(0,num-1)

    higher = data[indie]["follower_count"]
    lower = data[boomy][ "follower_count"]
    print(higher)
    print(lower)
    break