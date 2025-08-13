# lists - mutable - can be changed

def list_sum(L):
    total = 0
    for i in L:
        # cycles through your list 3 then 5 then 8
        total += i # adds those numbers together
    return total
    
myList = ([3,5,8])
print (list_sum(myList))

sen = "I am a big gorilla lost in the mist"
newSen = sen.split(' ')
newSen.sort()
print (newSen)

mylist = [4,7,1,8,3,9,2]
ordered_list = []
for i in mylist:
    mylist.remove(i)
    for j in (mylist):
        if i>j:
            mylist[j]=i
            i=j
    #mylist.append(i)
    ordered_list.append(i)
print(ordered_list)
