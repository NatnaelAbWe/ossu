def guess_sqrt(num):

    x = num
    low = 0
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
        print(f'The low becomes {low} and the high becomes {high}')
        
        guess = (high + low)/2.0
        num_guesses += 1

    print('num guesses =', num_guesses)
    print(guess, 'is clone to square root of', x)
    print(guess * guess)

guess_sqrt(1.5)



