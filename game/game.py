from constants.image import BACKGROUND_IMAGE
from game.player import Player 

class Game: 
  def __init__(self, screen): 
    self.screen = screen 
    self.player = Player() 

  def update(self): 
    pass

  def draw(self): 
    self.screen.blit(BACKGROUND_IMAGE, (0, 0))              
    self.player.draw(self.screen)