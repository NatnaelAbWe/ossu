x = 54321
epsilon = 0.01 
num_guesses = 0
guess = 0.0
increment = 0.01

while abs(guess ** 2 -x) >= epsilon and guess ** 2 <= x:
    guess += increment
    num_guesses += 1
print('number of guesses: ',num_guesses)

if abs(guess ** 2 -x) >= epsilon:
    print("Failed on square root of", x)
    print(f'The last guess was {guess}')
    print(f'The last guess squared was {guess * guess}')
else:
    print(guess, 'is clone to suquare root of ', x)
