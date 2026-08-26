from game_data import data
import art
import random
print(art.logo)
def ask_to_play():
    ask = input("want to play again: yes or no \n").lower()
    return ask == "yes"
def main_game():
    playing = True
    while playing:
        score =0
        again = True
        while again:       
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
            question = input("higher or lower\n").lower()
            if question == "higher":
                if values[1] > lower_value[1]:
                    score += 1
                    print(score)
                else:
                    print(f"u lost with final score {score}")
                    again = False
            elif question == "lower":
                if values[1] < lower_value[1]:
                    score += 1
                    print(score) 
                else:
                    print(f"{art.final} {score}")
                    again = False
            else:
                print("invalid input please enter higher or lower")
                continue
                    
        playing = ask_to_play()
main_game()
