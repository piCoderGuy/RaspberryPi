x = int(input('The number you would like to know the square root of: '))
epsilon = 0.0001 # Accuracy of output
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses +=1
print(f'num_guesses = {num_guesses}')

if abs(guess**2 - x) >= epsilon:
    print(f'Failed to find the root of {x}')
    print(f'Last guess was {guess}')
    print(f'Last guess squared is {guess**2}')

else:
    print(f'{guess} is close enough to the root of {x}')
