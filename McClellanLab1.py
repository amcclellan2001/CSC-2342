#!/usr/bin/env python3

__author__ = "Alex McClellan"
__copyright__ = "Copyright 2020"
__credits__ = ["Braeden Thompson, Jake Lorah, Justin Weiss, Justin Ricc, Ashlyn Hanks, Cam Bortle, Michael Blanchard"]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amcclell@highpoint.edu"
__status__ = "Development"
#Grade: C
#Note: I've had issues with different print statements not staying on the same line, such as with the truth tables and shifting through printing each true and false for the truth table. Justin Weiss helped us write the section of code with manipulating the variables from the user input.
    


def main():
    import re
    print("This program converts Propositional Logic problems into a truth table.\n")
    print("Enter in a propositional logic problem like: p \/ q (include spaces).\n")
    print("Connectives: /\ (And), \/ (Or), > (Implies)\n")
    
    #User input
    problem = input("What would you like the program to compute?\n").lower()
    
    #Check for correct input
    inputcheck = problem.isdigit()

    #Bugged with syntax error
    if inputcheck == True:
      print(problem.isdigit())
      print("Do not enter any numerical values, only propositional logic problems.\n")
      print("Please restart the program.\n")
        
    chunks = problem.split(' ')
  
    AND = '/\\'
    OR = '\/'
    IMP = '>'

    str = 'P /\ Q /\ r'

    #Lowercasing the user input strimng
    str = str.lower()
    chunks = str.split(' ')

    #Saving the count from the list
    count = len(chunks)

    #Testing
    #print(count)
    #print(chunks)

    #Getting a count of variables
    letters = chunks.copy()
    letters = list(dict.fromkeys(letters))

    #Separating operators from variables
    if AND in letters:
        letters.remove(AND)
    if OR in letters:
        letters.remove(OR)
    if IMP in letters:
        letters.remove(IMP)

    #Preparation for truth tables
    numbLetters = len(letters)
    #print(numbLetters)
    size = 2 ** numbLetters
    
    #Testing
    #print(size)
    #print(letters)

    #print("----------")

    #Holding onto the new string
    new = chunks.copy()
    new = list(dict.fromkeys(new))
    #print(new)
    temp = 0
    for x in range(count):
        if not (chunks[x] == AND or chunks[x] == OR):
            temp = temp + 1

    #print(temp)


    #Printing Tables
    print("----------")
    print("Printing Table")
    print("----------")
    print("Problem")
    #Printing Problem
    for x in range(count):
        #print(x)
        print(chunks[x])


        if chunks[x] == '/\\':
            print("and")

        elif chunks[x] == '\/':
            print("or")
            
        elif chunks[x] == '>':
            print("implies")
        
    
    #Printing True/False
    print("----------")
    row1 = 1
    row2 = 2
    
    for x in range(size):
        
        if (row1 % 2) == 0:
            print("T")
            ++row1
            
        elif (row1 % 2) != 0:
            print("F")
            ++row1
            
        if (row2 % 2) == 0:
            print("F")
            ++row2
            
        elif (row2 % 2) != 0:
            print("T")
            ++row2

        #print("\n")

if __name__ == "__main__":
    main()



