run = 1
while run == 1:
    x = int(input('The number you would like to know the square root of(0=exit): '))
    if x ==0:
        run = 0
    epsilon = 0.0001 # Accuracy of output
    num_guesses = 0
    low = 0.0001
    high = x
    guess = (high + low)/2.0
    increment = 0.000001
    if run == 1:
        while abs(guess**2 - x) >= epsilon:
            if (guess**2 < x):
                low = guess+increment
            else:
                high = guess
            guess = ((high + low)/2.0)+increment
            num_guesses +=1
        
        if abs(guess**2 - x) >= epsilon:
            print(f'Failed to find the root of {x}')
            print(f'Last guess was {guess}')
            print(f'Last guess squared is {guess**2}')

        else:
            print(f'{guess} is close enough to the root of {x}')
            print(f'{num_guesses} guesses used.')
