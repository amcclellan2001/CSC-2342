#!/usr/bin/env python3

__author__ = "Alex McClellan"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amcclell@highpoint.edu"
__status__ = "Development"
#Grade: C


def main():
    #Watch out for tuples (not defined compiler error)
    #Use array.append() method to add to array
    
    #Intro
    print("Welcome to the Unary Quantification program!\n")
    print("This program was made to compute problems like: x + y = 0 or x > 0\n")
    
    #Variables
    print("What variables would you like to use?\n")
    print("Examples: x | x & y\n")
    variables = input()
    
    #Function
    print("What is the function of the problem you would like to use?\n")
    print("Examples: x > 0 | x + y = 0\n")
    function = input()
    
    #Domain
    print("What is the domain of the problem you would like to use?\n")
    print("Examples: 1-10\n")
    domain = input()
    domain = int(domain)
    
    #Quantifiers
    print("What is the quantifier that you would like to use?\n")
    print("Examples: u (for Universal) | e (for Existential)\n")
    quantifier = input()
    
    #Splitting Function if there is a statement
    if function.isalpha() == False:
        first, second, third = function.split(' ')
    
        #Testing function
        if first.isdigit() == True:
            problem = first
            variable = third
        
        elif third.isdigit() == True:
            variable = first
            problem = third
        
        second = function
        
    #If it is an isolated variable for the function
    else:
        function = variable
    
    #Converting function for problem
    answer = 0
    
    if function == '>':
        calc = 'greater'
        
    elif function == '<':
        calc = 'less'
        
    elif function == '=':
        calc = 'equal'
       
    else:
        calc = 'variable'
        
    #Figuring out the problem to use
    result == True
    
    if calc == 'greater':
        answer = variable > problem
        
    elif calc == 'less':
        answer = variable < problem
        
    elif calc == 'equal':
        if domain == problem:
            bool([result]) == True
        
        else:
            bool([result]) == False
    
    #Universal quanitifer testing
    if quantifier == 'u':
        if answer > domain:
            bool([result]) == True
            
        else:
            bool([result]) == False
    
    #Existential quantifier testing
    else:
        if domain != answer:
            bool([result]) == False
            
        else:
            bool([result]) == True
    
    #Print the results
    print("The answer is: ")
    print([result])
    print("\n")
    

if __name__ == "__main__":
    main()
