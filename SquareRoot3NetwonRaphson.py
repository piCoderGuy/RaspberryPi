run = 1
while run == 1:
    x = int(input('The number you would like to know the square of(0=exit): '))
    if x ==0:
        run = 0
    epsilon = 0.0001 # Accuracy of output
    num_guesses = 0
    low = 0.0001
    high = x
    guess = x/2.0
    if run == 1:
        while abs(pow(guess,2) - x) >= epsilon:
            
            num_guesses +=1
            guess = guess -((pow(guess,2)-x)/(2*guess))
        if abs(pow(guess,2) - x) >= epsilon:
            print(f'Failed to find the Sq.R of {x}')
            print(f'Last guess was {guess}')
            print(f'Last guess, cube is {guess**2}')

        else:
            print(f'{guess} is close enough to the Sq.R of {x}')
            print(f'{num_guesses} guesses used.')


