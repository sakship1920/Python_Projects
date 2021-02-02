from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # 0 is for turn off animation

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < - 300:
        # need to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # deetect ball miss by right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect ball miss by left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
