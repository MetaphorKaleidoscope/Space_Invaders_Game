from turtle import Turtle
from shoot import Shoot


class Shoots(Turtle):
    def __init__(self):
        super().__init__()
        self.shoot = Shoot
        self.move_y = 10
        self.all_shoots = []

    def shooting(self, position, can_shot, side):
        if can_shot:
            self.shoot = Shoot(position)
            self.shoot.side = side
            self.all_shoots.append(self.shoot)

    def move(self):
        for shoot in self.all_shoots:
            if shoot.not_stop:
                new_y = shoot.ycor() + self.move_y * shoot.side
                shoot.goto(shoot.xcor(), new_y)

    def velocity(self):
        self.move_y += 1

    def remove_shoot(self, shoot):
        if shoot in self.all_shoots:
            shoot.goto(-3000, -3000)
            shoot.not_stop = False
            self.all_shoots.remove(shoot)
