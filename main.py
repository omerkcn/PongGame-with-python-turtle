from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_LOCATION = [(-350, 0), (350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle(PADDLE_LOCATION[0], "blue")
paddle_right = Paddle(PADDLE_LOCATION[1], "orange")
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")
screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")
speed = 0.005

game_is_on = True

while game_is_on:
    time.sleep(ball.time_speed)
    screen.update()
    ball.move()
    #Detect collision with top and bottom wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.xcor() > 320 and paddle_right.distance(ball) < 60 or paddle_left.distance(ball) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect right paddle's ball out of Bounds
    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.reset_position()

    # Detect right paddle's ball out of Bounds
    if ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.reset_position()

    if scoreboard.right_score == 3:
        scoreboard.game_over("Right player")
        game_is_on = False
    elif scoreboard.left_score == 3:
        scoreboard.game_over("Left player")
        game_is_on = False












screen.exitonclick()
