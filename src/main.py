import pygame

from constants import *
from player import Player


def main():
    # debug prints
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Get the return codes for passing and failing modules while init
    rc = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # init player to center of screen
    player_ship = Player(PLAYER_START_POS_X, PLAYER_START_POS_Y)

    while True:
        # Check for game close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update ship rotation
        player_ship.update(dt)

        # Draw background and ship
        screen.fill("black")
        player_ship.draw(screen)

        # Updates the screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000    # convert dt to seconds


if __name__ == "__main__":
    main()
