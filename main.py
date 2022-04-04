import pygame

screen=pygame.display.set_mode([600,600])
f=pygame.image.load("mysprites/dirt.jpg")
fheight=f.get_height()
screen.blit(f,[0,600-fheight])
pygame.display.flip()








while True:
   events= pygame.event.get()
   for event in events:
       if event.type == pygame.QUIT:
           exit()
