from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorebd = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebd.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() > 290 or snake.head.ycor() <-290:
        scorebd.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scorebd.reset()
            snake.reset()


screen.exitonclick()