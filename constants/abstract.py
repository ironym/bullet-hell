from abc import *

class GameObject(metaclass=ABCMeta): 
  @abstractmethod
  def update(self):
    pass
  
   @abstractmethod
  def draw(self, screen):
    pass