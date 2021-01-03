import pygame
import os

WIDTH = 800
HEIGHT = 600

pygame.init()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Space Invaders")
    ICON = pygame.image.load(os.path.join("imgs", "spaceship.png"))
    pygame.display.set_icon(ICON)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((0,0,128))
        pygame.display.update()

main()
