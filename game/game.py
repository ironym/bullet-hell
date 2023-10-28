from constants.image import BACKGROUND_IMAGE
class Game: 
  
  def __init__(self, screen): 
    self.screen = screen 
  
  def draw(self): 
    self.screen.blit(BACKGROUND_IMAGE, (0, 0))              