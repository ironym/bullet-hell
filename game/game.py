from constants.image import BACKGROUND_IMAGE
from game.player import Player 
from game.enemy import Enemy

class Game: 
  def __init__(self, screen): 
    self.screen = screen 
    self.player = Player()
    self.enemies = [ Enemy() ] 

  def update(self): 
    self.player.update()

    for enemy in self.enemies: 
      enemy.update()

  def draw(self): 
    self.screen.blit(BACKGROUND_IMAGE, (0, 0))              
    self.player.draw(self.screen) 

    for enemy in self.enemies: 
      enemy.draw(self.screen)