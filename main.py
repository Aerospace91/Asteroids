#Importing Pygame
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()