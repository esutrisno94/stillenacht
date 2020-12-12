from stillenacht.drawable import *
import sys

if __name__ == '__main__':
   INA = "INA"
   GER = "DE"
   if len(sys.argv) > 1:
      country = sys.argv[1]
      my_painting = Painting(country)
   else:
      my_painting = Painting()

   my_painting.draw()