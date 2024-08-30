import pygame

from constants import *


def main():
    # debug prints
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Get the return codes for passing and failing modules while init
    rc = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Check for game close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        # Updates the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
