# # yearly_salary = float(input("what is your yearly salary: "))
# # portion_saved = float(input("what is your saving from your salary: "))

# seen = ""
# s = "abca"

# for c in s:
#     if c in seen:
#         pass
#     else:
#         seen += c

# print(len(seen))

guesses = 0

x = int(input("enter a number: "))
while guesses ** 2 < x:
    guesses += 1
    if guesses ** 2 < x:
        pass
    elif guesses ** 2 == x:
        print(f'{x} is a perfect square of {guesses}')
    else:
        print(f'{x} is not a perfect square')