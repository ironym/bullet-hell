from constants.abstract import GameObject
from constants.image import ENEMY_IMAGE
from constants.setting import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(GameObject): 
    def __init__(self): 
        self.image = ENEMY_IMAGE  
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 70) 

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)