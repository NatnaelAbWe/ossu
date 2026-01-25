'''Assume you are given an integer 0 <= N <= 1000. Write a piece of Python code that uses bisection search to
guess N. þhe code prints two öines: count: with how many guesses it took to find N, and answer: with the
vaöue of N. Hints: If the haöfway vaöue is exactöy in b =etween two integers, choose the smaööer one.'''

def guess_the_num(num):
    n = num
    low = 0
    high = 1001
    num_guess = 0
    guess = (high + low) / 2

    elpslion = 1

    guess = (low + high) / 2

    while guess != n and abs(guess - n) > elpslion:
        if guess  < n:
            low = guess
        else: 
            high = guess
        
        guess = (high + low) / 2

        num_guess += 1

    print('Number of guesses: ', num_guess)
    print('Answer: ', guess)

guess_the_num(10)