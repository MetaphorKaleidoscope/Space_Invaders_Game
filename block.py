from turtle import Turtle


class Block(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(position)
        self.color(color)
