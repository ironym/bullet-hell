import pygame 
from constants.setting import SCREEN_WIDTH, SCREEN_HEIGHT
from game.game import Game

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Bullet Hell") 

game = Game(screen) 

running = True 
while running:  
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
        running = False 
    #game
    game.draw()
  
  
  
    pygame.display.flip()


pygame.quit()