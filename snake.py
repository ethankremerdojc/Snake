import pyglet

class Snake():
    def __init__(self):
        self.speed = 2  # blocks per second
        self.position = {"head": [12, 20], "body": [[11, 20], [10, 20], [9, 20], [8, 20]]}
        self.direction = "right"
        self.last_tail_position = [0, 0]

    def update_positions(self, new_position):
        new_position = {
            "head": new_position,
            "body": [self.position['head']] + self.position['body'][:-1]
        }
        self.last_tail_position = self.position['body'][-1]
        self.position = new_position

    def check_for_death(self, position, window_height, window_width):
        if position in self.position["body"]:
            self.kill()
        if position[0] < 0 or position[0] * 20 > window_width or position[1] < 0 or position[1] * 20 > window_height:
            self.kill()

    def move(self, direction, window_height, window_width):
        new_position = [-1, -1]

        if direction == "left":
            new_position[0] = self.position["head"][0] - 1
            new_position[1] = self.position["head"][1]

        if direction == "right":
            new_position[0] = self.position["head"][0] + 1
            new_position[1] = self.position["head"][1]

        if direction == "up":
            new_position[0] = self.position["head"][0]
            new_position[1] = self.position["head"][1] + 1

        if direction == "down":
            new_position[0] = self.position["head"][0]
            new_position[1] = self.position["head"][1] - 1

        self.check_for_death(new_position, window_height, window_width)
        self.update_positions(new_position)

    def draw(self):
        rectangles = []

        head_position = self.position['head']
        head_rectangle = pyglet.shapes.Rectangle(head_position[0] * 20, head_position[1] * 20, 20, 20)
        rectangles.append(head_rectangle)

        for bp in self.position['body']:
            rect = pyglet.shapes.Rectangle(bp[0] * 20, bp[1] * 20, 20, 20)
            rectangles.append(rect)

        for rect in rectangles:
            rect.draw()

    def kill(self):
        print("Player has died.")
        exit()