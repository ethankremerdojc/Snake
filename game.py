import pyglet
from snake import Snake
import random

window_width = 800
window_height = 800
window = pyglet.window.Window(width=window_width, height=window_height)

grid = [[[i,j] for j in range(40)] for i in range(40)]
snake = Snake()

def create_food():
    
    
    on_snake = True
    while on_snake == True:
        random_row = random.choice(grid)
        random_point = random.choice(random_row)
        print(f"created point {random_point}")
        if random_point in snake.position['body'] or random_point == snake.position['head']:
            # print('failed point')
            pass
        else:
            on_snake = False

    return pyglet.shapes.Rectangle(random_point[0] * 20, random_point[1] * 20, 20, 20, color=(255, 0, 0))

foods = [create_food() for i in range(3)]

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
    global foods, window_width, window_height
    snake.move(snake.direction, window_height, window_width)

    temp_foods = []

    for food in foods:
        if snake.position["head"] == [food.x / 20, food.y / 20]:
            snake.position['body'].append(snake.last_tail_position)

            temp_foods.append(create_food())
        else:
            temp_foods.append(food)
    
    foods = temp_foods

@window.event
def on_draw():
    window.clear()
    snake.draw()

    for food in foods:
        food.draw()

pyglet.clock.schedule_interval(update, 0.15)
pyglet.app.run()