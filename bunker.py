from turtle import Turtle
from block import Block


class Bunker(Turtle):
    def __init__(self):
        super().__init__()
        self.block = Block
        self.color_block = ['green']
        self.line_block = [0, 1, 2, 3]
        self.x_position = -200
        self.y_position = -200
        self.step_x = 11
        self.step_y = 11
        self.complete_bunker = []
        self.displacement = [0, 150, 300]

    def build_bunker(self):
        for step in self.displacement:
            self.x_position = -200 + step
            self.y_position = -200
            for _ in self.line_block:
                for _ in range(10):
                    self.block = Block((self.x_position, self.y_position), self.color_block)
                    self.complete_bunker.append(self.block)
                    self.x_position += self.step_x
                self.y_position += self.step_y
                self.x_position = -200 + step

    def remove_block(self, block):
        if block in self.complete_bunker:
            block.goto(-3000, -3000)
