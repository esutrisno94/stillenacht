import pygame

class AbstractCanvas:
    def draw_circle(self, x, y, color, diameter):
        pass
    def get_height(self):
        pass

class Canvas:
   BLACK = [0, 0, 0]
   WHITE = [255, 255, 255]
   GRAY = [50, 50, 50]
   LIGHTGRAY = [150,150,150]
   RED = [255, 0, 0]
   YELLOW = [0, 255, 0]

   def __init__(self, height=400, width=400):
       self.__height = height
       self.__width = width

       pygame.init()
       pygame.display.set_caption("Stillenact")

       self.__screen = pygame.display.set_mode([self.__width, self.__height])
       self.__clock = pygame.time.Clock()

   def get_height(self):
       return self.__height

   def reset_background(self):
       self.__screen.fill(Canvas.BLACK)

   def draw_circle(self, x, y, color, diameter):
       pygame.draw.circle(
           self.__screen,
           color,
           (x, y),
           diameter,
       )

   def is_quit(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return True

       return False

   def quit(self):
       pygame.quit()

   def flip(self):
       pygame.display.flip()
       self.__clock.tick(20)
