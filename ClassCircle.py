# Class Circle

class Circle(object):
    def __init__(self, x,y, radius):
        if type (x) != int:
            raise ValueError
        if type (y) != int:
            raise ValueError
        if type (radius) != int:
            raise ValueError
        self.center = center
        self.radius = radius
    
    #These two methods are the same, center of circle to point
    # or point to center of circle.
    def is_inside1(self, point):
        # if distance is inside radius return true else false
        return point.distance(self.center) < self.radius
        
    def is_inside2(self, point):
        # if distance is inside radius return true else false
        return self.center.distance(point) < self.radius
    
class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**2
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
center = (2,2)
my_circle = Circle (2,2, 5)
p
