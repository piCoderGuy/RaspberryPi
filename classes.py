# Classes
import math
import numpy as np
class Coordinates(object):
    # __init__ - initializes the object with the values given
    def __init__(self, xval, yval):
        # self - so these variables only belong to this object.
        # if you creat another obect using this class, it can have different x,y values
        self.x = xval
        self.y = yval
    def distance (self, other):
        #Pythagarus
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.x-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def reset_origin(self):
        self.x = 0
        self.y = 0
        
c =Coordinates(3,4)
origin = Coordinates (0,0)
for i in range (10):
    print (c.distance(origin))
    print(c.x+i)
    print(origin.x)
    c.reset_origin()
    #c.x = np.sin(c.x+i)
