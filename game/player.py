# game/player.py

import pygame
from constants.abstract import GameObject
from constants.image import PLAYER_IMAGE, SPRITE_FRAME_WIDTH, SPRITE_FRAME_HEIGHT
from constants.setting import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHIP_SPEED
from constants.direction import LEFT, RIGHT, UP, DOWN 

class Player(GameObject):
    def __init__(self):
      self.image = PLAYER_IMAGE
      self.rect = self.image.get_rect()
      self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
      
			# 속도, 방향 초기화
      self.direction = UP # <-----
      self.speed = 0 # <-----
      self.rotated_image = self.image

    def update(self): # <-----
      keys = pygame.key.get_pressed()
      if (keys[pygame.K_LEFT] and not self.rect[0] <= 0):
        self.direction = LEFT
        self.speed = PLAYER_SHIP_SPEED
      elif (keys[pygame.K_RIGHT] and not self.rect[0] >= SCREEN_WIDTH - SPRITE_FRAME_WIDTH):
        self.direction = RIGHT
        self.speed = PLAYER_SHIP_SPEED
      elif (keys[pygame.K_UP] and not self.rect[1] <= 0):
        self.direction = UP
        self.speed = PLAYER_SHIP_SPEED
      elif (keys[pygame.K_DOWN] and not self.rect[1] >= SCREEN_HEIGHT - SPRITE_FRAME_HEIGHT):
        self.direction = DOWN
        self.speed = PLAYER_SHIP_SPEED
      else:
        self.speed = 0
          
      self.rect.center = (self.rect.center[0] + self.direction.x * self.speed, self.rect.center[1] + self.direction.y * self.speed)
      self.rotated_image = pygame.transform.rotate(self.image, self.direction.angle)  

    def draw(self, screen):
      screen.blit(self.rotated_image, self.rect)
