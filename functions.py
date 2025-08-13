x=int(input('Enter a number: '))
y=int(input('Enter a 2nd number: '))
op=input('Type plus / minus / mult / div : ')

def calculation(op,x,y):
    return op(x,y)

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

#z=calculation(op,x,y)
if op == ('plus'):
    print (f' {x} {op} {y} = {calculation(plus,x,y)}')
if op == ('minus'):
    print (f' {x} {op} {y} = {calculation(minus,x,y)}')
if op == ('mult'):
    print (f' {x} {op} {y} = {calculation(mult,x,y)}')
if op == ('div'):
    print (f' {x} {op} {y} = {calculation(div,x,y)}')
