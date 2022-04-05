import pygame

screen=pygame.display.set_mode([600,600])
dirt=pygame.image.load("mysprites/dirt.jpg")
space=pygame.image.load("mysprites/space.jpg")
dirtheight=dirt.get_height()
screen.blit(space,[0,0])
screen.blit(dirt,[0,600-dirtheight])
pygame.display.flip()








while True:
   events= pygame.event.get()
   for event in events:
       if event.type == pygame.QUIT:
           exit()
