import pygame
# import random

class Vehicle:
    def __init__(self, name, direction, line):
        # Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(".\images\\" + self.name + ".png"), (50, 50))
        self.direction = direction
        self.line = line
        self.position_x = 375
        self.position_y = 20 + (line * 50)
        # self.go_right = ("police-car", "taxi", "motorbike")
        # self.go_left = ("bicycle", "van", "truck")
    
    def vehicleMove(self):
        if self.direction == "right":
            if self.position_x < 750:
                self.position_x += 2
            else:
                self.position_x = -50
        elif self.direction == "left":
            if self.position_x > -50:
                self.position_x -= 0.5
            else:
                self.position_x = 750
        