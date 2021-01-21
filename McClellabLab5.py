#!/usr/bin/env python3

__author__ = "Alex McClellan"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amcclell@highpoint.edu"
__status__ = "Development"



def main():

    print("This program tests whether an integer is prime or composite.")
    integer = int(input("Please input a positive integer for the program to test.\n"))
    
    #Input check
    while integer < 1:
        integer = input("Please enter a positive integer that is 1 or greater.")
        
    #Prime check
    composite = 0
    testnumber = 2

    #Checking operation
    for x in range (testnumber, integer-1):
        answer = integer % testnumber
    
        if answer == 0:
            composite += 1

            print("Composite detected. Composite number = ", testnumber)
        x += 1

    #Prime Printing
    if composite == 0:
        print(integer, "is a prime number.")

    else:
        print(integer, "is a composite number.")

if __name__ == "__main__":
    main()
