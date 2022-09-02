import pygame,random

class Cat(pygame.sprite.Sprites):
  def __init__(self,pos,images):
    super().__init__()
    self.images = images
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = [8,0]