from turtle import Turtle


class Ship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color('green')
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        self.penup()
        self.move = 70
        self.goto(position)
        self.can_shot = True

    def right_move(self):
        self.goto(self.xcor() + self.move, self.ycor())

    def left_move(self):
        self.goto(self.xcor() - self.move, self.ycor())

    def reset_position(self):
        self.goto(0, -230)

    def remove_ship(self):
        self.goto(-3000, -3000)
