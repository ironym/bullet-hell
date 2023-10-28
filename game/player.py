from constants.abstract import GameObject
from constants.image import PLAYER_IMAGE
from constants.setting import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(GameObject): 
    def __init__(self): 
        self.image = PLAYER_IMAGE 
        self.rect = self.image.get_rect() 
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  
    def update(self):
        pass

    def draw(self, screen): 
        screen.blit(self.image, self.rect)