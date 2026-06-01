import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangular Sprites")
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue
RED = (255, 0, 0)
BLUE = (0, 0, 255)
class RectangleSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
sprite1 = RectangleSprite(RED, 100, 80, 150, 250)
sprite2 = RectangleSprite(BLUE, 120, 60, 450, 250)
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)