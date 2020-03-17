import pygame

class Player:
    def __init__(self):
        # Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        self.image = pygame.transform.scale(pygame.image.load(".\images\man.png"), (50, 50))
        self.position_x = 350
        self.position_y = 20

    def hasColision(self):
        self.position_x = 350
        self.position_y = 20