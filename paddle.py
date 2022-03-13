from turtle import Turtle

PADDLE_LOCATION = [(-350, 0), (350, 0)]
MOVE_PADDLE = 40
PADDLE_EDGE_TOP = 245
PADDLE_EDGE_DOWN = -245


class Paddle(Turtle):

    def __init__(self, position_xy, paddle_color):
        super().__init__()
        self.shape("square")
        self.color(paddle_color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position_xy)

    def move_up(self):
        if self.ycor() < PADDLE_EDGE_TOP:
            y_cord = self.ycor() + MOVE_PADDLE
            self.goto(self.xcor(), y_cord)

    def move_down(self):
        if self.ycor() > PADDLE_EDGE_DOWN:
            y_cord = self.ycor() - MOVE_PADDLE
            self.goto(self.xcor(), y_cord)

