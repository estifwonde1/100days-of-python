class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
    def hello(self):
        print(f"hello{self.username}")
class Quiz:
    def __init__(self,question_id):
        self.id = question_id


user = User()
user.id = " 001"
user.username = "estif"
