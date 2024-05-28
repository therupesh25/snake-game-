from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score_board

s = Screen()
s.bgcolor("black")
s.setup(width=580, height=580)
s.title("snakegame")
s.tracer(0)
snake = Snake()
food = Food()
scoreboard = Score_board()

s.listen()
s.onkeypress(snake.up, "Up")
s.onkeypress(snake.down, "Down")
s.onkeypress(snake.right, "Right")
s.onkeypress(snake.left, "Left")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refersh()
        snake.extend_seg()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset()
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()

s.exitonclick()
