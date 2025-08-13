#Tuples - Immutable (can't be changed)
# a tuple is a list contained inside perenfeces() numbers or strings seperated by commas.
# use the [] to index into the tuple
# tpl[1:2] slices 2 list member and 2nd element after eg ,
# tpl[1:3] slice 2nd and 3rd elements
# len(tpl) returns number of elements in the tuple
# tuples can be nested inside tuples numbers = (1,2,3,4,(5,6,7),(8,9),(a,b,c))
# Tuple is one object so useful for returning multiple elments from a function.
def quotient_and_remainder(x, y):
    q=x//y	# (rounded)
    r=x%y
    return (q, r)

both = quotient_and_remainder(20, 3)
print (f'20 / 3 = {both[0]} with a remainder of {both[1]}')

s= str(input('Give me a word: '))

def char_counts(string):
    (c ,v) = (0,0)
    vowels = 'aeiou'
    for char in string:
        if char in vowels:
            v += 1
        else:
            c += 1
    return (v, c)
c = (char_counts(s))
print(f'{s} has {(c[0])} vowels & {(c[1])} consonants ')
