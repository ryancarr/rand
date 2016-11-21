# Random number generator
# Quickly generates numbers in a specified range
# and generates a specific quantity of random numbers
# Author: Ryan Carr
# Date  : 11/21/2016

from random import randint

def getInt(question):
    while True:
        inp = input(question)

        try:
            number = int(inp)
            break
        except:
            print('Please enter a valid whole number')

    return number

def main():
    minimum = getInt('What is the minimum value you want generated? ')
    maximum = getInt('What is the maximum value you want generated? ')
    quantity = getInt('How many random numbers do you want to generate? ')

    numbers = set()
    
    while len(numbers) < quantity:
        numbers.add(randint(minimum, maximum))

    numbers = list(numbers)
    numbers.sort()

    with open('rand_output.txt', 'w') as f:
        for number in numbers:
            f.write(str(number) + '\n')


if __name__ == '__main__':
    main()
