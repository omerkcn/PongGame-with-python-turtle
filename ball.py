from turtle import Turtle
STARTING_POSITION = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(STARTING_POSITION)
        self.x_move = 10
        self.y_move = 10
        self.time_speed = 0.1

    def move(self):
        x_cord = self.xcor() + self.x_move
        y_cord = self.ycor() + self.y_move
        self.goto(x_cord, y_cord)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.time_speed *= 0.7

    def reset_position(self):
        self.goto(0, 0)
        self.time_speed = 0.1
        self.bounce_x()



