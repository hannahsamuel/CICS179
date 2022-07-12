#  A guessing game: the user thinks of a number that the computer must guess
# Rules:
# > The computer must make no more than the minimum number of guesses, and
# it must prevent the user from cheating by entering misleading hints.


import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

max_guesses = math.ceil(math.log(larger - smaller,2))

count = 0
while True:
    count += 1
    if count > max_guesses:
        print("I'm out of guesses, and you cheated!")
        break
    print(smaller, larger)
    guess = (larger + smaller)//2
    print("Your number is", guess)
    answer = str(input("Enter =, <, or >: "))
    if answer == "<":
        larger = guess - 1
    elif answer == ">":
        smaller = guess + 1
    else:
        print("Hooray, I've got it in", count, "tries!")
        break