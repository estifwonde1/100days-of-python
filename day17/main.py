from questions import data_quiz_questions
import random
class User:
    def __init__(self ,user_id ):
        self.id = user_id
        self.score = 0
    def ask_question(self,score):
        num = len(data_quiz_questions)
        indie = random.randint(0,num-1)
        que = data_quiz_questions[indie]
        needed_data = ["question","answer"]
        values = [que[k] for k in needed_data]
        print(values[0])
        ask = input("True or False\n")
        if ask == values[1]:
            self.score += 1