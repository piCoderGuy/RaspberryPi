run = 1
while run == 1:
    x = int(input('The number you would like to know the cube of(0=exit): '))
    if x ==0:
        run = 0
    epsilon = 0.0001 # Accuracy of output
    num_guesses = 0
    low = 0.0001
    high = x
    guess = (high + low)/3.0
    increment = 0.000001
    if run == 1:
        while abs(pow(guess,3) - x) >= epsilon:
            if (pow(guess,3) < x):
                low = guess+increment
            else:
                high = guess
            guess = ((high + low)/2.0)+increment
            num_guesses +=1
        
        if abs(pow(guess,3) - x) >= epsilon:
            print(f'Failed to find the cube of {x}')
            print(f'Last guess was {guess}')
            print(f'Last guess, cube is {guess**2}')

        else:
            print(f'{guess} is close enough to the cube of {x}')
            print(f'{num_guesses} guesses used.')

