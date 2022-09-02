import pygame, sys
from pygame import *
from Sprite_loader import *

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (
    screen_info.current_w,
    screen_info.current_h,
)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 255, 255)
cat_images = []
def get_images():
  cat_sheet = SpriteSheet('runningcat.png')
  for i in range(4):
    for j in range(2):
      cat_images.append(cat_sheet.get_image(j*512,i*256,512,256))
      cat_images[-1] = pygame.transform.smoothscale(cat_images[-1],(180,90))

def main():
    get_images()
    cat_image = cat_images[0]
    cat_rect = cat_image.get_rect()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        frame = pygame.time.get_ticks() // 60 % 8
        cat_image = cat_images[frame]
        screen.fill(color)
        screen.blit(cat_image,cat_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
