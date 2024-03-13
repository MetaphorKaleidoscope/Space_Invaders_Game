# Space Invaders Game
from turtle import Screen
from bunker import Bunker
from aliens import Aliens
from mystery import Mystery
from ship import Ship
from shoots import Shoots
from scoreboard import Scoreboard
from lives import Lives
import time
import random


screen = Screen()
screen.setup(width=500, height=600)
screen.bgcolor("black")  # background color
screen.title("Space Invaders Game")
screen.tracer(0)  # Animation turn on

"""instructions
"""

# make a bunker
bunker = Bunker()
bunker.build_bunker()
# alien front
aliens = Aliens()
aliens.aliens_front()
# mystery
mystery = Mystery((-350, 230))

# ship
ship = Ship((0, -230))

# shoot
shoots_alien = Shoots()
shoots_ship = Shoots()

# scorebard
scoreboard = Scoreboard((200, -295))
# Lives
lives = Lives((-220, -295))

screen.listen()
screen.onkey(ship.right_move, 'Right')
screen.onkey(ship.left_move, 'Left')
screen.onkey(lambda: shoots_ship.shooting((ship.xcor(), ship.ycor()), ship.can_shot, 1), 'Up')


n = 0
m = 0
space_shot = 0
temp = 0
game_is_on = True
winner = 56
while game_is_on:

    # Game over Lives end
    if lives.live < 0:
        scoreboard.game_over()
        game_is_on = False

    space_shot += 1
    screen.update()
    time.sleep(0.05)
    n = aliens.right_left(n)
    m = mystery.right_left(m)

    if space_shot == 5:
        aliens_can_shot = [alien for alien in aliens.complete_aliens if alien.can_shot]
        alien_shoot = random.choice(aliens_can_shot)
        shoots_alien.shooting((alien_shoot.xcor(), alien_shoot.ycor()), alien_shoot.can_shot, -1)
        space_shot = 0
    # move shoots
    shoots_alien.move()
    shoots_ship.move()

    # check collisions
    # collision between bunker and shoots_aliens
    for shoot in shoots_alien.all_shoots:
        for block in bunker.complete_bunker:
            if shoot.distance(block) < 20:
                bunker.remove_block(block)
                shoots_alien.remove_shoot(shoot)

    # collision between bunker and shoots_ship
    for shoot in shoots_ship.all_shoots:
        for block in bunker.complete_bunker:
            if shoot.distance(block) < 20:
                bunker.remove_block(block)
                shoots_ship.remove_shoot(shoot)
                shoot.reset()

    # collision between shoot and ship
    for shoot in shoots_alien.all_shoots:
        if shoot.distance(ship) < 20:
            ship.remove_ship()  # add new live
            shoots_alien.remove_shoot(shoot)
            shoot.reset()
            lives.refresh()
            ship.reset_position()

    # collision between shoot_ship and aliens
    for alien in aliens.complete_aliens:
        for shoot in shoots_ship.all_shoots:
            if shoot.distance(alien) < 20:
                dir(alien)
                points = getattr(alien, 'points')
                scoreboard.refresh(points)
                winner -= 1
                aliens.remove_alien(alien)
                shoots_ship.remove_shoot(shoot)

    # collision between shoot and shoot
    for shoot_a in shoots_alien.all_shoots:
        for shoot_s in shoots_ship.all_shoots:
            if shoot_a.distance(shoot_s) < 10:
                shoots_alien.remove_shoot(shoot_a)
                shoots_ship.remove_shoot(shoot_s)

    # collision between shoot and mystery
    for shoot in shoots_ship.all_shoots:
        if shoot.distance(mystery) < 20:
            dir(mystery)
            points = getattr(mystery, 'points')
            scoreboard.refresh(points)
            winner -= 1
            mystery.remove_mystery()
            shoots_ship.remove_shoot(shoot)
            shoot.reset()

    # check if alien ship is down then next alien ship can shoot
    aliens.check_down_aliens()

    # check shoots_alien pass ship
    for shoot in shoots_alien.all_shoots:
        if shoot.ycor() < -300:
            shoots_alien.remove_shoot(shoot)

    # check shoots_ship pass aliens
    for shoot in shoots_ship.all_shoots:
        if shoot.ycor() > 300:
            shoots_ship.remove_shoot(shoot)

    # check if winner
    if winner == 0:
        scoreboard.you_winner()
        game_is_on = False

screen.exitonclick()
