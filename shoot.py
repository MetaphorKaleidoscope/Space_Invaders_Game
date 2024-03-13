from turtle import Turtle


class Shoot(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.1, stretch_wid=0.5)
        self.side = 1
        self.not_stop = True
        self.goto(position)
