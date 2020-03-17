# imports
import pygame
from Game import Game
from Player import Player
from Animal import Animal

# initialize PyGame
pygame.init()

# new game
game = Game()

# caption and icon
game.captionDisplay()
game.iconDisplay()

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
    game.display(game.background, 0, 0)

    for event in pygame.event.get():
        #quit option   
        if event.type == pygame.QUIT:
            game.running = False

        # controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.position_x > 0:
                player.position_x -= 50
            elif event.key == pygame.K_RIGHT and player.position_x < 700:
                player.position_x += 50
            elif event.key == pygame.K_UP and player.position_y > 20:
                player.position_y -= 50
            elif event.key == pygame.K_DOWN and player.position_y < 500:
                player.position_y += 50

    # player render
    game.display(player.image, player.position_x, player.position_y)   

    # animals moves and render
    for animal in animals_list:
        animal.animalMove()
        game.display(animal.image, animal.position_x, animal.position_y)
        # colision check
        if (player.position_x <= animal.position_x + 31 and player.position_x >= animal.position_x - 31) and player.position_y == animal.position_y:
            player.hasColision()

    # screen update
    game.render()

         