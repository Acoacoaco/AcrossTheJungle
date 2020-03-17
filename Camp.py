import pygame
import random

class Camp:
    def __init__(self):
        # Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        self.image = pygame.transform.scale(pygame.image.load("./images/camp.png"), (50, 50))
        self.position_x = random.choice(range(0, 701, 50))
        self.position_y = 520