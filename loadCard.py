import pygame
import setting
from Card import CardClass

class Card(pygame.sprite.Sprite):
    def __init__(self, name, position): 
        pygame.sprite.Sprite.__init__(self)
        self.name = CardClass(color, value)
        self.width = pygame.Surface.get_width(setting.screen)
        self.height = pygame.Surface.get_height(setting.screen)
        self.screen = pygame.display.set_mode((pygame.Surface.get_width(setting.screen), pygame.Surface.get_height(setting.screen)))
        self.image = pygame.image.load('./image/'+color+'_'+str(value)+'.png')
        self.image = pygame.transform.scale(self.image, (self.width*0.12,self.height*0.23))
        self.orig_pos = position
        self.position = position
        self.user_rotation = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.position