from questions import data_quiz_questions
import random
class User:
    def __init__(self ,user_id ):
        self.id = user_id
        self.score = 0
    def ask_question(self,score):
        play = True
        while play:
            num = len(data_quiz_questions)
            indie = random.randint(0,num-1)
            que = data_quiz_questions[indie]
            needed_data = ["question","answer"]
            values = [que[k] for k in needed_data]
            print(values[0])
            print(values[1])
            ask = input("True or False\n")
            answer = values[1]
            if ask == answer:
                self.score += 1
                print(score)
            elif ask != values[1]:
                print(f"wrong answer {score}")
                play = False
            else:
                print("invalidinput")
user1 = User("001")
user1.ask_question(0)