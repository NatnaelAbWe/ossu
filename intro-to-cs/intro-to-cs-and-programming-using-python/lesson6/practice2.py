# square root guessing 

def guess_sqrt(num):

    x = num
    epsilon = 0.01


    if x >= 1:
       low = 1.0
       high = x
    
    else:
        low = x
        high = 1.0

    guess = (high + low)/2.0
    num_guesses = 0 

    while abs(guess ** 2 - x) >= epsilon:
        if guess ** 2 > x:
            high = guess
        else:
            low = guess
        # print(f'The low becomes {low} and the high becomes {high}')
        
        guess = (high + low)/2.0
        num_guesses += 1

    print('num guesses =', num_guesses)
    print(guess, 'is clone to square root of', x)
    print(guess * guess)

guess_sqrt(1.5)


# cube root guessing

def guess_qubert(num):

    x = num
    epsilon = 0.01

    if x >= 1:
        low = 0
        high = x
    else:

        low = x
        high = 1.0

    guess = (low + high) / 2.0
    num_guesses = 0

    while abs(guess ** 3 - x ) >= epsilon:
        if guess ** 3 > x:
            high = guess
        else:
            low = guess
        # print(f'The low becomes {low} and the high becomes {high}')
        
        guess = (high + low)/2.0
        num_guesses += 1

    print('num guesses =', num_guesses)
    print(guess, 'is clone to cube root of', x)
    print(guess * guess * guess)

guess_qubert(-27)

# newton raphson algorithm

def newton_raphson(num):

    epsilon = 0.01
    k = num
    guesses = k / 2.0
    num_guesses = 0

    while abs(guess * guess -k) >= epsilon:
        num_guesses += 1
        guess = guess - (((guess ** 2) -k) / (2 * guess))
    print('num_guesses = ' + str(num_guesses))
    print('square root of ' + str(k) + ' is about '+ str(guess))



