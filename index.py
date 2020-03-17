import pygame
from Player import Player
from Animal import Animal

pygame.init()

screen = pygame.display.set_mode((750, 590))

pygame.display.set_caption("Across The Jungle")
# Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
icon = pygame.image.load(".\images\monkey.png")
pygame.display.set_icon(icon)

player = Player()

cheatah = Animal("cheatah", "left", 1)
crocodile = Animal("crocodile", "right", 2)
elephant = Animal("elephant", "left", 3)
horse = Animal("horse", "right", 4)
panda = Animal("panda", "left", 5)
monkey = Animal("monkey", "right", 6)
raccoon = Animal("raccoon", "left", 7)
lion = Animal("lion", "right", 8)
rhino = Animal("rhino", "left", 9)

animals_list = []

animals_list.append(cheatah)
animals_list.append(crocodile)
animals_list.append(elephant)
animals_list.append(horse)
animals_list.append(panda)
animals_list.append(monkey)
animals_list.append(raccoon)
animals_list.append(lion)
animals_list.append(rhino)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.position_x > 0:
                    player.position_x -= 50
            elif event.key == pygame.K_RIGHT and player.position_x < 700:
                    player.position_x += 50
            elif event.key == pygame.K_UP and player.position_y > 20:
                    player.position_y -= 50
            elif event.key == pygame.K_DOWN and player.position_y < 500:
                    player.position_y += 50

    for animal in animals_list:
        animal.animalMove()
        screen.blit(animal.image, (animal.position_x, animal.position_y))
    
    screen.blit(player.image, (player.position_x, player.position_y))

    pygame.display.update()
        