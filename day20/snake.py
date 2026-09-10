import turtle as t
import random

#setups
screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snakey cake")
screen.tracer(0)
score_board = t.Turtle()
score_board.hideturtle()
score = 0
score_board.color("white")
score_board.penup()
score_board.speed("fastest")
score_board.shapesize(1,1)
score_board.setpos(0,270)
score_board.write(score,font =("ariel",20,"bold"))
food = t.Turtle("circle")
food.color("green")
food.shapesize(0.5,0.5)
food.penup()
x_pos = random.randint(-290,290)
y_pos = random.randint(-290,290)
food.speed("fastest")
food.setpos(x_pos,y_pos)
head = t.Turtle(shape="square")
head.penup()
head.color("white")

segement_postions = [(-20,0),(-40,0)]
fully = []
for _ in segement_postions:
    snakey = t.Turtle(shape = "square")
    snakey.color("white")
    snakey.penup()
    snakey.goto(_)
    fully.append(snakey)

pos_history =[]
step_delay = 3
def move():
    pos_history.insert(0,head.pos())
    head.forward(10)
    head.speed(1)
    for index,snakey in enumerate(fully):
        history = (index + 1) *3
        if len(pos_history) > history:
            snakey.goto(pos_history[history])
    # if len(pos_history) > 20:
    #     pos_history.pop()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        screen.exitonclick()
    if head.distance(food) < 15:
        n = -60
        global score
        x_pos = random.randint(-290,290)
        y_pos = random.randint(-290,290)
        food.clear()
        food.goto(x_pos,y_pos)
        score_board.clear()          
        score += 1
        score_board.write(score,font =("ariel",20,"bold"))
        snakey = t.Turtle(shape = "square")
        snakey.color("white")
        snakey.penup()
        snakey.goto(head.xcor(),head.ycor())
        fully.append(snakey)
        n += -20
        print (n,head.ycor())

        print(head.position(),food.position())
    screen.update()
    screen.ontimer(move,20)
def move_right():
    new_heading = head.heading() + 90
    head.setheading(new_heading)
def move_left():
    new_heading = head.heading() - 90
    head.setheading(new_heading)
is_gameover = True


move() 
   

#yeah am really confused on how i can move all 3 blocks getting dictated by the first 1 as head
#the trick is to use the fronts postion change to be the next ones change and so on and i will try to figure that out tommorrow but for today solid work proud of myself   



screen.listen()
screen.onkey(key ="a",fun = move_right)
screen.onkey(key = "d",fun = move_left)















screen.exitonclick()