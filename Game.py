import pygame

class Game:
    def __init__(self):
        # screen properties
        self.screen = pygame.display.set_mode((750, 590))

        # game loop
        self.running = True

        # background
        # <a href="https://www.freepik.com/free-photos-vectors/logo">Logo vector created by valadzionak_volha - www.freepik.com</a>
        self.background = pygame.image.load("./images/background.png")
        
        # caption
        self.caption = "Across The Jungle"

        # level
        self.level = 0

        # icon
        # Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        self.icon = pygame.image.load("./images/monkey.png")

        # change music
        self.can_change_music = 1

        # insturctons text properties
        self.instructions = pygame.font.Font("./fonts/FreeSansBold.ttf", 13) 

        # win text properties
        self.win = pygame.font.Font("./fonts/FreeSansBold.ttf", 50) 
    
    # caption and icon display
    def captionDisplay(self):
        pygame.display.set_caption(self.caption)

    def iconDisplay(self):
        pygame.display.set_icon(self.icon)
    
    # draw
    def draw(self, image, position_x, position_y):
        self.screen.blit(image, (position_x, position_y))

    # screen update
    def display(self):
        pygame.display.update()

    # show instructions
    def showInstructions(self):
        return self.instructions.render("Use keyboard arrows to get to the camp. Avoid animals!", True, (255, 255, 255))

    # show instructions2
    def showInstructions2(self):
        return self.instructions.render("Press ENTER, if you want to play on the next level.", True, (255, 255, 255))
   
    # show instructions2
    def showLevel(self):
        return self.instructions.render("Danger level: " + str(self.level), True, (255, 0, 0))

    # controls
    def operations(self, move_left, move_right, move_up, move_down):
        for event in pygame.event.get():
        #quit option   
            if event.type == pygame.QUIT:
                game.running = False

            # controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left
                elif event.key == pygame.K_RIGHT:
                    move_right
                elif event.key == pygame.K_UP:
                    move_up
                elif event.key == pygame.K_DOWN:
                    move_down

    # colision check
    def colisionCheck(self, player_position_x, player_position_y, animal_position_x, animal_position_y):
        if (player_position_x <= animal_position_x + 31 and player_position_x >= animal_position_x - 31) and player_position_y == animal_position_y:
            return True

    # camp check
    def isInCampCheck(self, player_position_x, player_position_y, camp_position_x, camp_position_y):
        if player_position_x == camp_position_x and player_position_y == camp_position_y:
            return True

    # show win text
    def showWinText(self):
        return self.win.render("You are safe in the camp!", True, (255, 255, 255))

    # play music
    def playMusic(self, title):
        # https://www.freesoundeffects.com/
        pygame.mixer.music.stop()
        # load music
        self.music = pygame.mixer.music.load("./music/" +title+ ".wav")
        # play music
        pygame.mixer.music.play(-1)
