word = input("Type a word: ")
seen = ''
for char in word:
    if char not in seen:
        seen = seen + char
print ("There are " + str(len(seen)) + " unique characters in " + word)
print (f"There are {len(seen)} unique characters in the word {word}")
