from turtle import Turtle


class Alien(Turtle):
    def __init__(self, position, shape, points):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.goto(position)
        self.color('green')
        self.right(90)
        self.can_shot = False
        self.points = points
