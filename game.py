import pyglet
from pprint import pprint
from snake import Snake
import time
import random

window_width = 800
window_height = 800
window = pyglet.window.Window(width=window_width, height=window_height)

grid = [[[i,j] for j in range(40)] for i in range(40)]
snake = Snake()

def create_food():
    global grid, snake
    on_snake = True
    print('Attempting to create food')
    while on_snake == True:
        random_row = random.choice(grid)
        random_point = random.choice(random_row)
        print(f"created point {random_point}")
        if random_point in snake.position['body'] or random_point == snake.position['head']:
            print('failed point')
        else:
            on_snake = False

    return pyglet.shapes.Rectangle(random_point[0] * 20, random_point[1] * 20, 20, 20, color=(255, 0, 0))

food = create_food()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.RIGHT:
        if snake.direction != 'left':
            snake.direction = 'right'
    if symbol == pyglet.window.key.LEFT:
        if snake.direction != 'right':
            snake.direction = 'left'
    if symbol == pyglet.window.key.UP:
        if snake.direction != 'down':
            snake.direction = 'up'
    if symbol == pyglet.window.key.DOWN:
        if snake.direction != 'up':
            snake.direction = 'down'

def update(dt):
    global food, window_width, window_height
    snake.move(snake.direction, window_height, window_width)
    if snake.position["head"] == [food.x / 20, food.y / 20]:
        snake.position['body'].append(snake.last_tail_position)
        food = create_food()

@window.event
def on_draw():
    window.clear()
    snake.draw()
    food.draw()

pyglet.clock.schedule_interval(update, 0.08)
pyglet.app.run()