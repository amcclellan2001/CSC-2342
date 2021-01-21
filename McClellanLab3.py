#!/usr/bin/env python3

__author__ = "Alex McClellan"
__copyright__ = "Copyright 2020"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amcclell@highpoint.edu"
__status__ = "Development"
#Note: For the onto operation, sometimes I get an error message that the list index is out of range when one list is longer than the other, and I'm not sure what would be the way to get around the error.

def main():
  
  print("This program is used to compute sets with element assignments.\n")
  print("Please enter a type of set to compute, either c for a character set, or i for integer set.\n")
  
  #Adding in sets and checking cardinality
  #Detects either character or integer set
  settype1 = input()
  
  if settype1 == "c":
    print("You have selected a character set.\n")
    elements = input("Please enter a list of characters separated by spaces.\n").split(' ')
        
    settype1 = "character"
    elementslist = []
    for i in elements:
        elementslist.append(i)
        
  #If it is an integer set
  else:
        print("You have selected an integer set.\n")
        elements = input("Please enter a list of integers separated by spaces.\n").split(' ')
       
        settype1 = "integer"
        elementslist = []
        for i in elements:
            elementslist.append(i)
    
  #Multiple Sets
  print("Would you like to add another set?\n")
  print("Please enter y for yes or n for no.\n")
  option = input()
  
  #User adding in another set
  if option == "y":
    print("Please enter a type of set to compute, either c for a character set, or i for integer set.\n")
    settype2 = input()
      
    if settype2 == "c":
        print("You have selected a character set.\n")
        elements2 = input("Please enter a list of characters separated by spaces.\n").split(' ')
            
        settype2 = "character"
        elements2list = []
        for i in elements2:
            elements2list.append(i)
         
    else:
        print("You have selected an integer set.\n")
        elements2 = input("Please enter a list of integers separated by spaces.\n").split(' ')
            
        settype2 = "integer"
        elements2list = []
        for i in elements2:
            elements2list.append(i)

  else:
        print("Continuing...\n")
        elements2list = elementslist

  set1card = len(elements)
  set2card = len(elements2)
  
  #Figuring out which set is larger
  if set1card > set2card:
    largercard = set1card
    shortercard = set2card
    
  else:
    largercard = set2card
    shortercard = set2card


  #Selecting a function
  print("There are a few options to compute sets: Onto and One-to-One.\n")
  print("Please enter either (onto) or (one-to-one) for the computation.\n")
  
  operation = input()
  
  #One-to-One Operation
  if operation == "one-to-one":
    print("You have selected a one-to-one operation.\n")
    print("Combing the first",settype1,"set with the second",settype2,"set.\n")
    
    for x in range(0, largercard):
        print(elementslist[x]," -> ",elements2list[x],"\n")
    
  #Onto Operation
  else:
    print("You have selected an onto operation.\n")
    print("Combing the second",settype2,"set with the first",settype1,"set.\n")

    if set1card == set2card:
        for y in range(0, set2card):
            print(elements2list[y]," -> ",elementslist[y],"\n")
        
    else:
        for z in range(0, shortercard):
            print(elements2list[z]," -> ",elementslist[z],"\n")
        
        print(elements2list[z]," -> ",elementslist[largercard],"\n")
            
  
if __name__ == "__main__":
    main()
