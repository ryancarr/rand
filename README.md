# rand
Random number generator in Python 3.x

## Known Issues
Very little error checking is implemented.
It is possible to break the program in a variety of ways, easiest is entering a larger number for min and smaller number for max.
Also if **quantity > (max - min)** the program will enter an infinite loop and run until user forces it closed with Ctrl+C
