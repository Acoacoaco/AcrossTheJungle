import pygame
from Player import Player

pygame.init()

screen = pygame.display.set_mode((750, 590))

pygame.display.set_caption("Cross the street")
# Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
icon = pygame.image.load(".\images\gamepad.png")
pygame.display.set_icon(icon)

player = Player()


running = True
while running:
    screen.fill((155, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player.position_x > 0:
                    player.position_x -= 50
            elif event.key == pygame.K_RIGHT:
                if player.position_x < 700:
                    player.position_x += 50
            elif event.key == pygame.K_UP:
                if player.position_y > 20:
                    player.position_y -= 50
            elif event.key == pygame.K_DOWN:
                if player.position_y < 500:
                    player.position_y += 50
  
    screen.blit(player.image, (player.position_x, player.position_y))
    pygame.display.update()
        