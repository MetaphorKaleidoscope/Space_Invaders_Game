from turtle import Turtle
from alien import Alien


class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.alien = Alien
        self.shape_alien = ['classic', 'classic', 'arrow', 'triangle', 'circle']
        self.x_position = -200
        self.y_position = 50
        self.step_x = 30
        self.step_y = 30
        self.move = 2
        self.complete_aliens = []

    def aliens_front(self):
        n = 1
        for shape in self.shape_alien:
            if shape == 'classic':
                points = 10
            elif shape == 'arrow':
                points = 20
            elif shape == 'triangle':
                points = 30
            else:
                points = 40
            for _ in range(11):
                self.alien = Alien((self.x_position, self.y_position), shape, points)
                self.complete_aliens.append(self.alien)
                self.x_position += self.step_x
                if n == 1:
                    self.alien.can_shot = True
            n += 1
            self.y_position += self.step_y
            self.x_position = -200

    def right_left(self, n):
        n += 1
        if n > 100:
            self.move *= -1
            n = 1
        for ufo in self.complete_aliens:
            ufo.goto(ufo.xcor() + self.move, ufo.ycor())
        return n

    def remove_alien(self, alien):
        if alien in self.complete_aliens:
            alien.goto(-3000, -3000)

    def check_down_aliens(self):
        a = 0
        b = 11
        for _ in range(3):
            for i in range(11):
                if self.complete_aliens[i + a].distance(self.complete_aliens[i + b]) > 1000:
                    self.complete_aliens[i+b].can_shot = True
            a = b
            b = b + a
