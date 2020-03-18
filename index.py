# imports
import pygame
from Game import Game
from Player import Player
from Animal import Animal
from Camp import Camp

# initialize PyGame
pygame.init()

# new game
game = Game()

# caption and icon
game.captionDisplay()
game.iconDisplay()

# new camp
camp = Camp()

# new player
player = Player()

# animals
cheatah = Animal("cheatah", "left", 1)
crocodile = Animal("crocodile", "right", 2)
elephant = Animal("elephant", "left", 3)
giraffe = Animal("giraffe", "right", 4)
panda = Animal("panda", "left", 5)
monkey = Animal("monkey", "right", 6)
raccoon = Animal("raccoon", "left", 7)
lion = Animal("lion", "right", 8)
rhino = Animal("rhino", "left", 9)

# animals list
animals_list = []

animals_list.append(cheatah)
animals_list.append(crocodile)
animals_list.append(elephant)
animals_list.append(giraffe)
animals_list.append(panda)
animals_list.append(monkey)
animals_list.append(raccoon)
animals_list.append(lion)
animals_list.append(rhino)

# gameloop
while game.running:
    # background color
    game.screen.fill((255, 255, 255))

    # background image
    game.draw(game.background, 0, 0)

    # instructions
    game.draw(game.showInstructions(), 10, 10)

    # level
    game.draw(game.showLevel(), 650, 10)

    # camp draw
    game.draw(camp.image, camp.position_x, camp.position_y)

    # player draw
    game.draw(player.image, player.position_x, player.position_y)   

    # music
    if game.can_change_music == 1:
        game.playMusic("jungle")
        game.can_change_music = 2
	
    for event in pygame.event.get():
        #quit option   
        if event.type == pygame.QUIT:
            game.running = False

        # controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moveLeft()
            elif event.key == pygame.K_RIGHT:
                player.moveRight()
            elif event.key == pygame.K_UP:
                player.moveUp()
            elif event.key == pygame.K_DOWN:
                player.moveDown()
            elif event.key == pygame.K_RETURN:
                game.level += 1
                if not player.can_move:
                    game.can_change_music = 1
                    camp.__init__()
                    player.__init__()
                    cheatah.__init__("cheatah", "left", 1)
                    crocodile.__init__("crocodile", "right", 2)
                    elephant.__init__("elephant", "left", 3)
                    giraffe.__init__("giraffe", "right", 4)
                    panda.__init__("panda", "left", 5)
                    monkey.__init__("monkey", "right", 6)
                    raccoon.__init__("raccoon", "left", 7)
                    lion.__init__("lion", "right", 8)
                    rhino.__init__("rhino", "left", 9)
                    for animal in animals_list:
                        animal.speed = animal.speed * game.level
                    

    # animals moves and render
    for animal in animals_list:
        animal.animalMove()
        game.draw(animal.image, animal.position_x, animal.position_y)
        # colision check
        if game.colisionCheck(player.position_x, player.position_y, animal.position_x, animal.position_y):
            player.makeSound()
            player.__init__()

    # is man in camp?
    if game.isInCampCheck(player.position_x, player.position_y, camp.position_x, camp.position_y):
        player.can_move = 0
        #  win text
        game.draw(game.showWinText(), 65, 200)
        game.draw(game.showInstructions2(), 215, 250)
        for animal in animals_list:
            animal.position_y = 2000
        if game.can_change_music == 2:
            game.playMusic("camp")
            game.can_change_music = 0
    # screen update
    game.display()
