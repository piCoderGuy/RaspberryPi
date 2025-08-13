# Dictionaries
# list example
# ['ABC','DEF',GHI','JKL']
# name = ['Name',['ps',[8,4,5,]],[mq, [6,7]]]
# def get_grades(who, what, data):
# 	for student in data:
# 		if student = [0] == who:
# 			for info in student[1:]:
# 				if info[0] == what:
# 					return who, info
# print (get_grades('Name', 'ps', grades)

# Dictionary example
def find_grades(grades, students):
    newList = []
    # Element is student in dictionary
    for element in students:
        grade = grades[element]
        newList.append(grade)
    return newList

grades = {'Anne':'A', 'Bob':'A', 'Mike':'B','Phil':'D'}
grades['Grace'] = 'A'
grades['Phil'] = 'B'
del(grades['Anne'])
print (find_grades(grades,['Bob', 'Phil']))

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3= {1:1, 3:9, 4:16, 5:25}

def find_inL(Ld, k):
    ''' Look through lots of dictionaries for 'k (integer)'
    return True if k is in dictionary or else False
    '''
    for a in Ld:	# a is element in each dictionary
        
        if k in a:
            return True
        
    return False

print (find_inL([d1, d2, d3], 2))

list (grades.keys()) # returns names in dictionary i.e.(['Anne', 'Bob', 'Phil'...
list (grades.values()) # returns the grades (['A', 'B', 'C'...
list (grades.items()) # returns tuples of each item in grades

for k,v in grades.items():		#	k is key, v is value
    print (f'Student {k} has achieved grade {v}')

d4 = {1:2,'a':'a', 5:5}

def count_matches(d):
    '''
    How many entries match 'd'
    '''
    count = 0
    counts = 0
    for v,k in d.items():
        if v==k:
            count +=1
    return count 
    for x in d.keys():
        if d[x]==x:
            counts+=1
    return counts
print (count_matches(d4))

# Frequency dictionary


def generate_word_dict(song):
    song_words = song.lower()
    words_list = song_words.split()		# convert string to list.
    word_dict = {}
    for w in words_list:
        if w in word_dict:		# If 'w' (word) is in list ...
            word_dict[w] += 1	# if yes, frequency increased by 1
        else:					# Strings are mapped to intergers
            word_dict[w] = 1	# First time seen? count is 1.
    return word_dict

song = "da do do do da da da da is all I want to say to you"
word_dict = generate_word_dict(song)
print (word_dict)
