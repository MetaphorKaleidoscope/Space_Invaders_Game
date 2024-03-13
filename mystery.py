from turtle import Turtle


class Mystery(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color('red')
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        self.penup()
        self.move = 5
        self.points = 100
        self.goto(position)

    def right_left(self, n):
        n += 1
        if n > 150:
            self.move *= -1
            n = 1
        self.goto(self.xcor() + self.move, self.ycor())
        return n

    def remove_mystery(self):
        self.goto(-3000, -3000)
