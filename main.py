import pygame
import constants, circleshape, player, sys
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from constants import *
from shot import *
def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player_1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    print("Starting asteroids!")

    

    while True:
        dt = (game_clock.tick(60) / 1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_1.shoot()
        
        
        
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player_1):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()

        
            
        
        
            


        screen.fill((0,0,0))

        for object in drawable:
            object.draw(screen)

    
        
        pygame.display.flip()

        

    
    
    
    
    
    #print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

    