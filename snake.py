import pprint
import os
import sys
import pickle
import pyglet

class Snake():

    def __init__(self, starting_position):
        self.speed = 2  # blocks per second
        self.position = starting_position
        self.direction = "right"
        self.last_tail_position = [0, 0]

    def update_positions(self, new_position):
        new_position = {
            "head": new_position,
            "body": [self.position['head']] + self.position['body'][:-1]
        }
        self.last_tail_position = self.position['body'][-1]
        self.position = new_position

    def check_for_death(self, window_width, window_height, other_player_position):
        if self.position['head'] in self.position["body"]:
            self.kill()

        if self.position['head'][0] < 0 or self.position['head'][0] * 20 > window_width or self.position['head'][1] < 0 or self.position['head'][1] * 20 > window_height:
            self.kill()

        if self.position['head'] in other_player_position['body'] or self.position['head'] == other_player_position['head']:
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

        self.update_positions(new_position)

    def draw(self, pcolor):

        rectangles = []

        head_position = self.position['head']
        head_rectangle = pyglet.shapes.Rectangle(head_position[0] * 20, head_position[1] * 20, 20, 20)
        rectangles.append(head_rectangle)

        for bp in self.position['body']:
            rect = pyglet.shapes.Rectangle(bp[0] * 20, bp[1] * 20, 20, 20, color=pcolor)
            rectangles.append(rect)

        for rect in rectangles:
            rect.draw()

    def kill(self):
        print("Player has died.")
        exit()