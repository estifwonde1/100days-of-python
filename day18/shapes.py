import random
from turtle import Screen, Turtle

mini = Turtle()
mini.shape()
colors = ["crimson","darkorange","gold","forestgreen","darkcyan","deepskyblue","royalblue","hotpink","saddlebrown"]
def randoming():
    pick = random.randint(0,len(colors)-1)
    randomize = colors[pick]
    mini.color(randomize)
    print(randomize)
def main():
   
    def draw_shape(num_sides):
        angle = 360/num_sides
        for _ in range(num_sides):    
            mini.forward(100)
            mini.right(angle)
    for _ in range(3,13):
        draw_shape(_)
        randoming()




        





    screen = Screen()
    screen.exitonclick()
if __name__ == "__main__":
    main()
