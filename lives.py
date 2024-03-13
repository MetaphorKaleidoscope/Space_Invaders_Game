from turtle import Turtle
ALIGNMENT = "center"


class Lives(Turtle):

    def __init__(self, position):
        super().__init__()
        self.live = 3
        self.penup()
        self.color('white')
        self.goto(position)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'{self.live}', align=ALIGNMENT, font=('OCR-A BT', 18, 'bold'))
        self.live -= 1
