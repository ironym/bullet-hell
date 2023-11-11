import random
import math
import pygame
from constants.abstract import GameObject
from constants.image import ENEMY_IMAGE
from constants.setting import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SHIP_SPEED
from constants.direction import Direction

class Enemy(GameObject): 
    def __init__(self): 
        self.image = ENEMY_IMAGE  
        self.__init_status()

    def __init_status(self): 
      initial_positions = [
        (-20, random.randint(0, SCREEN_HEIGHT)), 
        (SCREEN_WIDTH + 20, random.randint(0, SCREEN_HEIGHT)),
        (random.randint(0, SCREEN_WIDTH), -20),
        (random.randint(0, SCREEN_WIDTH), SCREEN_HEIGHT + 20),
      ]

      initial_x, initial_y = random.choice(initial_positions)

      target_x = SCREEN_WIDTH // 2 + random.randint(-50, 50) 
      target_y = SCREEN_HEIGHT // 2 + random.randint(-50, 50) 

      direction_x = target_x - initial_x 
      direction_y = target_y - initial_y 

      length = math.sqrt(direction_x ** 2 + direction_y ** 2)
      
      direction = Direction(direction_x / length, direction_y / length)
      angle_radians = math.atan2(-direction.y, direction.x)
      angle_degrees = math.degrees(angle_radians)

      self.rect = self.image.get_rect()
      self.rect.center = (initial_x, initial_y)
      self.x = initial_x 
      self.y = initial_y
      self.direction = direction 
      self.speed = ENEMY_SHIP_SPEED 
      self.rotated_image = pygame.transform.rotate(self.image, 90 + angle_degrees)

    def update(self): 
        self.x += self.speed * self.direction.x 
        self.y += self.speed * self.direction.y
        self.rect.x = self.x
        self.rect.y = self.y
        

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rect)