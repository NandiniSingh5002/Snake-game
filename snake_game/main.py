from turtle import Screen, Turtle
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()  # update screen when our all box is moved
    time.sleep(0.1)  # only get delay 0.1 sec after all segment moved
    snake.move()

screen.exitonclick()
