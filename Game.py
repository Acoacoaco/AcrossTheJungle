import pygame

class Game:
    def __init__(self):
        # screen properties
        self.screen = pygame.display.set_mode((750, 590))

        # game loop
        self.running = True

        # background
        # <a href="https://www.freepik.com/free-photos-vectors/logo">Logo vector created by valadzionak_volha - www.freepik.com</a>
        self.background = pygame.image.load(".\images\\background.png")
        
        # caption
        self.caption = "Across The Jungle"

        # icon
        # Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        self.icon = pygame.image.load(".\images\monkey.png")

        # font properties
    
    # caption and icon display
    def captionDisplay(self):
        pygame.display.set_caption(self.caption)

    def iconDisplay(self):
        pygame.display.set_icon(self.icon)
    
    def display(self, image, position_x, position_y):
        self.screen.blit(image, (position_x, position_y))


    # screen update
    def render(self):
        pygame.display.update()