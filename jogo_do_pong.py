import turtle

player_left_score = 0
player_right_score = 0
ballxdirection = 0.15
ballydirection = 0.15

ws = turtle.Screen()
ws.title("Jogo do Pong")
ws.bgcolor("black")
ws.setup(width=800, height=600)
ws.tracer(0)

left_racket = turtle.Turtle()
left_racket.speed(0)
left_racket.shape("square")
left_racket.color("red")
left_racket.shapesize(stretch_wid=5, stretch_len=1)
left_racket.penup()
left_racket.goto(-350, 0)

right_racket = turtle.Turtle()
right_racket.speed(0)
right_racket.shape("square")
right_racket.color("red")
right_racket.shapesize(stretch_wid=5, stretch_len=1)
right_racket.penup()
right_racket.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Left: {}    Player Right: {}".format(player_left_score, player_right_score), align="center", font=("Arial", 24, "normal"))

def left_racket_up():
    y = left_racket.ycor()
    y += 20
    if y < 250:
        left_racket.sety(y)

def left_racket_down():
    y = left_racket.ycor()
    y -= 20
    if y > -240:
        left_racket.sety(y)

def right_racket_up():
    y = right_racket.ycor()
    y += 20
    if y < 250:
        right_racket.sety(y)

def right_racket_down():
    y = right_racket.ycor()
    y -= 20
    if y > -240:
        right_racket.sety(y)

ws.listen()
ws.onkeypress(left_racket_up, "w")
ws.onkeypress(left_racket_down, "s")
ws.onkeypress(right_racket_up, "Up")
ws.onkeypress(right_racket_down, "Down")

while True:
    ws.update()

    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ballydirection *= -1

    if (340 > ball.xcor() > 330) and (right_racket.ycor() + 50 > ball.ycor() > right_racket.ycor() - 50):
        ball.setx(330)
        ballxdirection *= -1

    if (-330 > ball.xcor() > -340) and (left_racket.ycor() + 50 > ball.ycor() > left_racket.ycor() - 50):
        ball.setx(-330)
        ballxdirection *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        player_left_score += 1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        player_right_score += 1

    pen.clear()
    pen.write("Player Left: {}    Player Right: {}".format(player_left_score, player_right_score), align="center", font=("Arial", 24, "normal"))
