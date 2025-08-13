run = 1
while run == 1:
    guess = 0
    x = int(input("Enter a number:(0 to exit) "))
    if x == 0:
        run = 0
    if run == 1:
        while guess**2 < x:
            guess += 1
        if guess**2 == x:
            print(f"{x} is a perfect square.")
        else:
            print (f'{x} is not a perfect square')
