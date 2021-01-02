import turtle
import winsound

# Setup game windows
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)


# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# B A L L
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("Player A: " + str(score_1) + "  PlayerB: " + str(score_2), align="center",
          font=("Courier", 24, "normal"))

# Functions


def paddle1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# keybord ninding
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

# Main loop
while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 375:
        ball.sety(375)
        ball.dy *= -1
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player A: " + str(score_1) + "  PlayerB: " + str(score_2), align="center",
                  font=("Courier", 24, "normal"))
        winsound.PlaySound(
            'score.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player A: " + str(score_1) + "  PlayerB: " + str(score_2), align="center",
                  font=("Courier", 24, "normal"))
        winsound.PlaySound(
            'score.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    if ball.ycor() < -375:
        ball.sety(-375)
        ball.dy *= -1
    # Colison for paddle
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(
            'hit.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() > paddle_1.ycor() - 50 and ball.ycor() < paddle_1.ycor() + 50)):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(
            'hit.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
