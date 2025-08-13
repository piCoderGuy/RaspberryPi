# Aliasing and copying
# [:] - copies a list
# del(L[index]) delete an element at a certain location
# L.pop() remove last element can also remove element in certain location L.pop(3)
# L.remove - remove an item that matches criteria ie L.remove(your_name) - only removes first element
# using the = sign makes an alias of the list ie aliasMyList = myList, any changes will be applied to both lists.

def remove_all(L, e):
    '''
    Remove all number 2's from list
    '''
    Lnew = L[:]	# create a copy of list
    L.clear()	# Now a empty list
    for n in Lnew:
        if e != n:
            L.append(n)
            
def remove_duplicates(L1,L2):
    '''
    to remove duplicates you must make a copy and delete the elements from the original.
    '''
    L1_copy = L1[:]
    for element in L1_copy:
        if element in L2:
            L1.remove(element)


L = [1,2,3,2,2,4,5,2,6,7,8,9]
remove_all(L, 3)
print (L)

L.remove(5)
print (L)
L.pop()	#	removed = L.pop() if you want to save the removed element to a variable
print(L)
L1 = L[:]
L2 = [2,4,7]
remove_duplicates(L1,L2)
print(L1)
# Alias-shallow and deep copy
old_list= [[1,2,3],[4,5,6],[7,8,9]]
new_list = old_list
#new_list = copy.deepcopy(old_list)
old_list.append([11,12,13])
print (old_list)
print(new_list)

def f(L):
    for element in L:
        if element %2 == 0:	# if numbers are even
            Lnew.append(element ** 2)
    return Lnew
# can be written as Lnew = [e ** 2 for e in L]
# Lnew [e ** 2 for e in L if e%2==0]
# [e **2 for e in range (6)] 			returns [0,1,4,9,16,25]
# [e **2 for e in range(8)if e%2== 0]	returns [0,4,16,36]
# [[e, e**2] for e in range (4) ife != %2]	returns [[1,1],[3,9]]
lenx = [len(x) for x in ['xy', 'abcd', 7, '4.2'] if type(x) == str]
print (lenx)
