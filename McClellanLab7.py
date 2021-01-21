#!/usr/bin/env python3

__author__ = "Alex McClellan"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amcclell@highpoint.edu"
__status__ = "Development"
import random


def main():
    #User input
    print("This program computes the probabiltiy of a coin flip.")
    flips = input("How many times should the program flip the coin?\n")
    heads = input("How many times should those flips be heads?\n")
    
    #Variables
    coin = 0
    probability = (heads + "/" + flips)
    
    head = int(heads)
    flip = int(flips)
    tail = flip - head
    
    percentage = (head / flip) * 100
    roundpercentage = round(percentage, 2)
    headcount = 0
    tailcount = 0
    
    #Computation
    for i in (0, flip):
        coin = random.randint(0, 1)
        
        if coin == 0:
            headcount += 1
        
        else:
            tailcount += 1

    

    #Output
    print("The coin was flipped", flips, "times.")
    print("In this attempt, the coin:")
    print("Landed on heads", headcount, "times.")
    print("Landed on tails", tailcount, "times.")
    print("The probability given the input is:", probability)
    print("The percentage of the probability is:", roundpercentage)


if __name__ == "__main__":
    main()
