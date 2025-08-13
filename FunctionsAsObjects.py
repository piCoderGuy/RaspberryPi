#Functions asobjects

def bisection_root(x, epsilon=0.01):	# default of epsilon= 0.01 if no value given
    #epsilon = 0.01
    low = 0
    high =x
    guess = (high+low)/2.0
    while abs (guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

print (bisection_root(123))
print (bisection_root(123, 0.0001))

# Functions returning Functions

def grab_number(a):
    def multiply_numbers(b):
        return a*b
    return multiply_numbers		# The function is returned which multiplys a&b (2)

numberA = grab_number(4)		# number A is passed to the function (1)
numberB = numberA(5)			# number B uses the returned function multiply_numbers (3)
print (numberB)

# Test and debug

def is_pal(x):
    temp = x
    temp.reverse()
    print(temp, x)
    
word = 'abcd'
is_pal(word)
