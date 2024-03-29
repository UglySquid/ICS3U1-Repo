# I - Import and Initialize
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))


class Box(pygame.sprite.Sprite):
    """Our Box class inherits from the Sprite class"""
    def __init__(self):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image attribute for our Box sprite
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill((255, 0, 0))
        
        # Set the rect attribute for our Box sprite
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 200
        self.__direction = 10

    def update(self):
        self.rect.left += self.__direction
        if (self.rect.left < 0) or (self.rect.right > screen.get_width()):
            self.__direction = -self.__direction

            
def main():
    """This function defines the 'mainline logic' for our game."""
    
    # Display
    pygame.display.set_caption("Basic Sprite Demo")
    
    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    screen.blit(background, (0,0))
    
    # create a Box sprite object
    box = Box()
    allSprites = pygame.sprite.Group(box)
    
    # ACTION
    
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Loop
    while keepGoing:
    
        # Time
        clock.tick(30)
    
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
    
        pygame.display.flip()
   
    # Close the game window
    pygame.quit()        
        

# Call the main function
main()