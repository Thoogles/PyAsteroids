import pygame

from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

    # Create groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # init player to center of screen
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    player_ship = Player(PLAYER_START_POS_X, PLAYER_START_POS_Y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    while True:
        # Check for game close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update all updatable objects
        for updates in updatable:
            updates.update(dt)

        # check for collision
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_detection(asteroid):
                    asteroid.split()
                    shot.kill()
            if asteroid.collision_detection(player_ship):
                print("Game over!")
                return

        # Draw background and drawable objects
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)

        # Updates the screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # convert dt to seconds


if __name__ == "__main__":
    main()
