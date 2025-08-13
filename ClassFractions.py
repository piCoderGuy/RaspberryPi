# Class Fraction
class Fraction(object):
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
        
    def __mul__(self, other):
        top = self.numerator*other.numerator
        bottom = self.denominator*other.denominator
        return Fraction(top,bottom)	#returns Fraction 'type'
    def __float__(self):
        return self.numerator/self.denominator
    
    def reduce(self):
        def gcd(n, d):
            while d != 0:
                (d,n) = (n%d,d)
            return n
        if self.denominator == 0:
            return None
        elif self.denominator ==1:
            return Fraction(self.numerator,1)
        else:
            greatest_common_divisor = gcd(self.numerator, self.denominator)
            top = int(self.numerator/greatest_common_divisor)
            bottom = int(self.denominator/greatest_common_divisor)
            return Fraction(top, bottom)

    
class SimpleFraction(object):
    def __init__ (self, n, d):
        self.numerator = n
        self.denominator = d
        
    def times(self, oth):
        top = self.numerator*oth.numerator
        bottom = self.denominator*oth.denominator
        
        return top/bottom
    
    def plus(self, oth):
        top = self.numerator*oth.denominator + self.denominator*oth.numerator
        bottom = self.denominator*oth.denominator
        
        return top/bottom
    
    def get_inverse(self):
        # Returns a float representing 1/self
        return self.denominator/self.numerator
    
    def invert(self):
        # Sets self's numerator to denominator and vice versa.
        # Returns None
        (self.numerator, self.denominator) = (self.denominator, self.numerator)
        #newdenom = self.numerator
        #newnum = self.denominator
        #self.numerator = newnum
        #self.denominator = newdenom
        return self.numerator/self.denominator

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
    
f1 = SimpleFraction (3,4)
f2 = SimpleFraction (3,4)
print(f1.numerator)
print(f1.denominator)
print(f1.plus(f2))
print(f1.times(f2))

print(f1.get_inverse())	# SHould print 1.3333333333
f1.invert()							# acts on data attributes internall and returns none
print(f1.numerator, f1.denominator)	# prints 4 3

c = Coordinate(3,4)
print(c)
print (type(c))
