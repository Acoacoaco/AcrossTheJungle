import pygame

class Player:
    def __init__(self):
        # Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        self.image = pygame.transform.scale(pygame.image.load(".\images\man.png"), (50, 50))
        self.position_x = 350
        self.position_y = 20

    # controls
    def moveLeft(self):
        if self.position_x > 0:
            self.position_x -= 50
    
    def moveRight(self):
        if self.position_x < 700:
            self.position_x += 50

    def moveUp(self):
        if self.position_y > 20:
            self.position_y -= 50

    def moveDown(self):
        if self.position_y < 500:
            self.position_y += 50
                