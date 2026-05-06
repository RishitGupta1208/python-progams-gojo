import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
background=pygame.transform.scale(pygame.image.load("bg.jpeg"),(300,300))
pygame.display.set_caption("game screen")
done=False
all_sprite=pygame.sprite.Group()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.blit(background,(0,0))
    all_sprite.draw(screen)
    pygame.display.flip()
pygame.quit()