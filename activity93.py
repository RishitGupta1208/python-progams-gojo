import pygame
pygame.init()
import pygame
pygame.init()
background=pygame.transform.scale(pygame.image.load('background.png'),(500,500))
pygame.display.set_caption("rectangle")
my_font = pygame.font.SysFont("Times New Roman", 30)
text_surface = my_font.render("Rectangle!", True, (0, 255,0))
screen=pygame.display.set_mode((500,500))
done=False
all_sprite=pygame.sprite.Group()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.blit(background,(0,0))
    screen.blit(text_surface, (10,10))
    all_sprite.draw(screen)
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(100,100,70,60))
    pygame.display.flip()
pygame.quit()