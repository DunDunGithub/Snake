from select import select
from turtle import Turtle
from random import randint, choice

from requests import head

start_position = [(0,0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(300, -300)
        self.goto(300, 300)
        self.goto(-300, 300)
        self.goto(-300, -300)
        self.hideturtle()

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for p in start_position:
            my_turtle = Turtle(shape='square')
            my_turtle.color(choice(colors))
            my_turtle.penup()
            my_turtle.goto(p)
            self.segments.append(my_turtle)

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[s-1].xcor()
            new_y = self.segments[s-1].ycor()
            self.segments[s].goto(new_x, new_y)
        self.segments[0].forward(20)

    def upLength(self):
        my_turtle = Turtle(shape='square')
        my_turtle.color(choice(colors))
        my_turtle.penup()
        temp_x = self.segments[len(self.segments) - 1].xcor()
        temp_y = self.segments[len(self.segments) - 1].ycor()
        if self.head.heading() == UP:
            my_turtle.goto(x = temp_x, y = temp_y - 20)
        elif self.head.heading() == DOWN:
            my_turtle.goto(x = temp_x, y = temp_y + 20)
        elif self.head.heading() == RIGHT:
            my_turtle.goto(x = temp_x - 20, y = temp_y)
        elif self.head.heading() == LEFT:
            my_turtle.goto(x = temp_x + 20, y = temp_y)
        self.segments.append(my_turtle)

    def lose(self):
        isCheck = True
        if self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 300 or self.head.ycor() <= -300:
            return False

        for s in self.segments[1:]:
            if self.head.distance(s) < 10:
                return False
        return isCheck         

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Apple(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('yellow')
        self.speed('fastest')
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x = random_x, y = random_y)

    def move(self):
        self.penup()
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x = random_x, y = random_y)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
    def show(self):
        self.write(f"Your score: {self.score}   High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.penup()
        self.goto(0, 320)
        self.color('white')
        self.hideturtle()
    def plus(self):
        self.score += 10
    def message(self):
        self.color('white')
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show()