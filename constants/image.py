import pygame

BACKGROUND_IMAGE = pygame.image.load('assets/background.png')



SPRITE_FRAME_WIDTH = 32 
SPRITE_FRAME_HEIGHT = 32 

PLAYER_IMAGE = pygame.image.load('assets/player-ship.png').subsurface(pygame.Rect (0, 0, SPRITE_FRAME_WIDTH, SPRITE_FRAME_HEIGHT)) 
ENEMY_IMAGE = pygame.image.load('assets/enemy-ship.png').subsurface(pygame.Rect (0, 0, SPRITE_FRAME_WIDTH, SPRITE_FRAME_HEIGHT)) 
