import pyglet
from pprint import pprint
from snake import Snake
import time
import random

window_width = 800
window_height = 800
window = pyglet.window.Window(width=window_width, height=window_height)

grid = [[[i,j] for j in range(40)] for i in range(40)]
player1 = Snake({"head": [12, 20], "body": [[11, 20], [10, 20], [9, 20], [8, 20], [7, 20]]})
player2 = Snake({"head": [12, 10], "body": [[11, 10], [10, 10], [9, 10], [8, 10], [7, 10]]})

def create_food():
    global grid, player1, player2
    on_snake = True
    print('Attempting to create food')
    while on_snake == True:
        random_row = random.choice(grid)
        random_point = random.choice(random_row)
        print(f"created point {random_point}")
        if random_point in player1.position['body'] or random_point == player1.position['head'] or random_point in player2.position['body'] or random_point == player2.position['head']:
            print('failed point')
        else:
            on_snake = False

    return pyglet.shapes.Rectangle(random_point[0] * 20, random_point[1] * 20, 20, 20, color=(255, 100, 100))

food = create_food()

@window.event
def on_key_press(symbol, modifiers):
    # Player 1
    if symbol == pyglet.window.key.RIGHT:
        player1.direction = 'right'
    if symbol == pyglet.window.key.LEFT:
        player1.direction = 'left'
    if symbol == pyglet.window.key.UP:
        player1.direction = 'up'
    if symbol == pyglet.window.key.DOWN:
        player1.direction = 'down'

    # Player 2
    if symbol == pyglet.window.key.D:
        player2.direction = 'right'
    if symbol == pyglet.window.key.A:
        player2.direction = 'left'
    if symbol == pyglet.window.key.W:
        player2.direction = 'up'
    if symbol == pyglet.window.key.S:
        player2.direction = 'down'

def update(dt):
    global food, window_width, window_height
    player1.move(player1.direction, window_height, window_width)
    player2.move(player2.direction, window_height, window_width)

    player1.check_for_death(window_width, window_height, player2.position)
    player2.check_for_death(window_width, window_height, player1.position)

    if player1.position["head"] == [food.x / 20, food.y / 20]:
        player1.position['body'].append(player1.last_tail_position)
        food = create_food()

    if player2.position["head"] == [food.x / 20, food.y / 20]:
        player2.position['body'].append(player1.last_tail_position)
        food = create_food()

@window.event
def on_draw():
    window.clear()
    player1.draw((100, 100, 255))
    player2.draw((0, 255, 100))
    food.draw()

pyglet.clock.schedule_interval(update, 0.3)
pyglet.app.run()