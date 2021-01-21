#!/usr/bin/env python3

__author__ = "Alex McClellan"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amcclell@highpoint.edu"
__status__ = "Development"
import math


def main():
    
    #Collecting user input for computation
    print("This program calculates combinations and permutations.")
    order = input("Does order of output matter in this computation? Enter either: True | False\n")

    #Combination, order is false
    if order == "False":
        #Getting initial set
        print("This program will calculate the combinations in two or more sets.")
        print("Please input a set of values, separated by spaces.")
        setaNumbers = input()
        aSumNumbers = 0
        aProductNumbers = 0
        setaSum = setaNumbers.split(' ')
        setaProduct = setaNumbers.split(' ')
        
        for i in setaSum:
            aSumNumbers += int(i)
            
        for i in setaProduct:
            aProductNumbers *= int(i)
            
        print("Sum Rule: ", aSumNumbers)
        print("Product Rule: ", aProductNumbers)
        
        print("Please input another set of values, separated by spaces.")
        setbNumbers = input()
        bSumNumbers = 0
        bProductNumbers = 0
        setbSum = setbNumbers.split(' ')
        setbProduct = setbNumbers.split(' ')
        
        for i in setbSum:
            bSumNumbers += int(i)
            
        for i in setbProduct:
            bProductNumbers *= int(i)
            
            
        print("Sum Rule: ", bSumNumbers)
        print("Product Rule: ", bProductNumbers)
        
        #Optional sets
        another = "y"
        
        while another == "y":
            print("Would you like to enter another list?")
            another = input("Type y to add another list, enter anything else to continue.")
            
            if another == "y":
                print("Please input another set of values, separated by spaces.")
                setcNumbers = input()
                cSumNumbers = 0
                cProductNumbers = 0
                setcSum = setcNumbers.split(' ')
                setcProduct = setcNumbers.split(' ')
                
                for i in setcSum:
                    cSumNumbers += int(i)
                
                for i in setcProduct:
                    cProductNumbers *= int(i)
                    
                print("Sum Rule: ", cSumNumbers)
                print("Product Rule: ", cProductNumbers)
    
            
        
            
    #Permutation, order is true
    else:
        #Getting initial set and size
        print("This program will calculate the permutation of a set and the size of the subset.")
        print("Please input a set of values, separated by spaces.")
        setnumbers = input().split(' ')
        
        for i in setnumbers:
            set = int(i)
        
        print("Please input the size of the subset.")
        sizeinput = input()
      
        size = int(sizeinput)
      
        #Getting the permutation with the size specified
        length = 0
        length = len(setnumbers)
        
        if (length != size):
            number = length - size
        
            permutation = math.factorial(set) / math.factorial(number)
            
            print("The permutation of the set with the specified size is: ", permutation)
        
        #If size is zero
        elif size == 0:
            print("When the size is 0, or an empty set, the answer is 1.")
        
        #Factorial, total possible options for the set
        else:
            factorial = length
        
            print("The total possible options of the set is: ", math.factorial(factorial))
            
            
if __name__ == "__main__":
    main()
