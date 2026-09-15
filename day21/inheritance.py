class Animal:
    def __init__(self):
        self.eyes = 2
    def breathing(self):
        print("inhale exhale")



class Fish(Animal):
    def __init__(self):
        super().__init__()
    
