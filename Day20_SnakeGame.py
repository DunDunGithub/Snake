import time
from turtle import Turtle, Screen, color
from Snake import Apple, Line, ScoreBoard, Snake

# SET SCREEN
screen = Screen()
screen.title('Snake Game')
screen.setup(width=700, height=800)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
apple = Apple()
score = ScoreBoard()
my_turtle = Line()

screen.listen()

screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# turtle_position = [(0,0), (-20, 0), (-40, 0)]

game_is_on = True

bonus = False

while game_is_on:

    score.show()
    screen.update()
    time.sleep(0.1)

    snake.move()
    if apple.distance(snake.head) < 15:
        apple.move()
        snake.upLength()
        score.clear()
        score.plus()
        score.show()
    game_is_on = snake.lose()
    if game_is_on == False:
        lose = ScoreBoard()
        lose.message()

screen.exitonclick()
