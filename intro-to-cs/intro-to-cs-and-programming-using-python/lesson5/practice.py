

# num = int(input("enter your number: "))

def binary_converter(num):
    if num < 0:
        is_neg = True
        num = abs(num)
    else:
        is_neg = False

    result = ''

    if num == 0:
        result = '0'

    while num > 0:
        result = result + str(num%2)
        num = num // 2

    if is_neg:
        result = '-' + result

    rev_result = int(str(result)[::-1])
    
    print(rev_result)

    return rev_result

# binary_converter(num)

def decimal_binary_converter(num): 
     x = num
     p = 0

    # 1. Scale x until it's an integer
    # Added a safety limit (p < 20) to prevent infinite loops
     while ((2**p) * x) % 1 != 0 and p < 20:
        p += 1

     num = int(x * (2**p))
     result = binary_converter(num)


    # 3. Add leading zeros if necessary
     for i in range(p - len(result) + 1):
      result = '0' + result

    # 4. Re-insert the decimal point safely
     if p > 0:
        result = result[:-p] + '.' + result[-p:]
     else:
        result = result + '.0'

     print(f'The binary representation of {x} is {result}')


# Approximation Method

g = 0.0
x = 54321
e = 0.01
i = 0.0001
no_guess = 0

while abs(g ** 2 - x) >= e and g ** 2 <= x:
    g += i
    no_guess += 1

print("The number of guesses:",no_guess)

if abs(g ** 2 - x) >= e:
    print(f'failed on square root of {x}')
    print(f'The last guess was {g}')
    print(f'The last squared guess is {g*g}')
else:
    print(g, "is close to the sqrt of ",x)

    ''' the big picture from this lecture is that don use == when comparing floating value and their might be a trade of f btwn the accuracy and the precision of the result and the approximation method becomes too slow when the number to be sqr rooted increases and the increment value too small'''

    '''======================= THE END ==============================='''