from questions import data_quiz_questions
import random
class User:
    def __init__(self ,user_id ):
        self.id = user_id
        self.score = 0
    def ask_question(self,score):
        needed = random.choice(data_quiz_questions["questions","answer"])
        if ask == data