num = int(input("enter your number: "))

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

is_neg = True

print(result)