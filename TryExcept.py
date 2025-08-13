# Exceptions and assertions

def sum_digits(s):
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print (f'Invalid, {char} is not a number!')
    return total

x =(sum_digits("123abc"))
print (x)

def inputA():
    try:
        print ('Lets multiply two numbers')
        a = int(input("Input 1st number: "))
        b = int(input("Input 2nd number: "))
    
    except:
        print("Invalid, please try again: ")
        return None
    x = a*b    
    return x

def inputB():
    try:
        print('Lets divide two numbers.')
        a = int(input("Input 1st number: "))
        b = int(input("Input 2nd number: "))
        
    except ValueError:
        print('That\'s not a number!')
        return 0.0
    
    try:
        x=a/b
    except ZeroDivisionError:
        print('I can\'t divide by zero.')
        print('Returns infinity.')
        print('a+b = ', a+b)
        return 0.0
    try:
        x=a/b
    except:
        print('Unknown error.')
    return x

while True:
    a = inputA()
    
    print (a)
    
    b = inputB()
    print (b)
