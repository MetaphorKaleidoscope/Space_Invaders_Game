from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(position)
        self.hideturtle()
        self.refresh(self.score)
        self.zeros = ''

    def refresh(self, points):
        self.clear()
        if self.score < 10:
            self.zeros = '000'
        elif self.score < 100:
            self.zeros = '00'
        elif self.score < 1000:
            self.zeros = '0'
        else:
            self.zeros = ''
        self.score += points
        self.write(f'{self.zeros}{self.score}', align=ALIGNMENT, font=('OCR-A BT', 18, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER ', align=ALIGNMENT, font=('OCR-A BT', 18, 'bold'))

    def you_winner(self):
        self.goto(0, 0)
        self.write(f'YOU WINNER ', align=ALIGNMENT, font=('OCR-A BT', 18, 'bold'))
