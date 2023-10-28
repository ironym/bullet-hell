import pygame 
from constants.setting import SCREEN_WIDTH, SCREEN_HEIGHT


pygame.init()



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Bullet Hell") 

running = True 
while running:  
  for event in pygame.event.get(): 
   if event.type == pygame.QUIT: 
    running = False 

   pygame.display.flip()

pygame.quit() 