from constants.image import BACKGROUND_IMAGE
from game.player import Player 
from game.enemy import Enemy
import random
import math

class Game: 
  def __init__(self, screen): 
    self.screen = screen 
    self.player = Player()
    self.enemies = [ Enemy() ] 

  def __is_collided(self, rect1, rect2, boundary_distance): 
    distance = math.sqrt((rect1.center[0] - rect2.center[0]) ** 2 + (rect2.center[1] - rect1.center[1]) ** 2)
    return distance < boundary_distance

  def update(self): 
    self.player.update()

    for enemy in self.enemies: 
      enemy.update()

    if random.randint(1, 100) < 3: 
      self.enemies.append(Enemy()) 

    new_enemies = [] 

    for enemy in self.enemies:
      if self.__is_collided(self.player.rect, enemy.rect, 15):
        continue
      new_enemies.append(enemy)
    
    self.enemies = new_enemies

  def draw(self): 
    self.screen.blit(BACKGROUND_IMAGE, (0, 0))              
    self.player.draw(self.screen) 

    for enemy in self.enemies: 
      enemy.draw(self.screen) 