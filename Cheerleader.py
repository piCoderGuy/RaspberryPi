run = 1
while run == 1:
    an_letter = 'aefhilmnorsxAEFHILMNORSX'
    word = input("Give me a word to cheer about(q=quit): ")
    if word == 'q':
        print ('Quitting')
        run = 0
    if run == 1:  
        level = int(input("Level of enthusiasm (1-9)"))

        for w in word:
            if w in an_letter:
                #print("Give me an " + w +": " + w)
                print(f'Give me an {w}: {w}')
                
            else:
                #print("Give me a " + w +": " + w)
                print(f'Give me a {w}: {w}')
        print("What does that spell?")
        for i in range (level):
            print (word, "!!!")
