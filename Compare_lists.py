
def f(L, L1, L2):
    inL1 = False
    for i in range (len(L1)):
        if L[i] == L1[i]:
            inL1 = True
            
    inL2 = False
    for i in range (len(L2)):
        if L[i] == L2[i]:
            inL2 = True
            
    return inL1, inL2	# return not inL1, not inL2 returns opposite result.


L = [1,3,5,7,9,10,11,12,13]
L1 = [2,4,6,8,14,15,16,17,13]
L2 = [1,2,3,4,5,6,7,8,9]

list1, list2 = f(L,L1,L2)
print (f"List 1 has elements in main list {list1}")
print (f"List 2 has elements in main list {list2}")
