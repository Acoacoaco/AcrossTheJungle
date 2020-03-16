import pygame
from Player import Player
from Vehicle import Vehicle

pygame.init()

screen = pygame.display.set_mode((750, 590))

pygame.display.set_caption("Cross the street")
# Icons made by <a href="https://www.flaticon.com/authors/flat-icons" title="Flat Icons">Flat Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
icon = pygame.image.load(".\images\gamepad.png")
pygame.display.set_icon(icon)

player = Player()
turtle = Vehicle("turtle", "left", 1)
bird = Vehicle("bird", "right", 2)
bicycle = Vehicle("bicycle", "left", 3)
taxi = Vehicle("taxi", "right", 4)
truck = Vehicle("truck", "left", 5)
police_car = Vehicle("police-car", "right", 6)
van = Vehicle("van", "left", 7)
motorbike = Vehicle("motorbike", "right", 8)
unicorn = Vehicle("unicorn", "left", 9)

running = True
while running:
    screen.fill((100, 100, 100))
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
    
    turtle.vehicleMove()
    bird.vehicleMove()
    bicycle.vehicleMove()
    taxi.vehicleMove()
    truck.vehicleMove()
    police_car.vehicleMove()
    van.vehicleMove()
    motorbike.vehicleMove()
    unicorn.vehicleMove()

    screen.blit(player.image, (player.position_x, player.position_y))
    screen.blit(turtle.image, (turtle.position_x, turtle.position_y))
    screen.blit(bird.image, (bird.position_x, bird.position_y))
    screen.blit(bicycle.image, (bicycle.position_x, bicycle.position_y))
    screen.blit(taxi.image, (taxi.position_x, taxi.position_y))
    screen.blit(truck.image, (truck.position_x, truck.position_y))
    screen.blit(police_car.image, (police_car.position_x, police_car.position_y))
    screen.blit(van.image, (van.position_x, van.position_y))
    screen.blit(motorbike.image, (motorbike.position_x, motorbike.position_y))
    screen.blit(unicorn.image, (unicorn.position_x, unicorn.position_y))
    pygame.display.update()
        