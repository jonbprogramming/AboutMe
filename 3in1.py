"""
Author: Jonathan Brown
Description: A program that will offer a user a choice to run one of three programs for their use."""

def print_instructions():
    print("This program will offer you three different equations for your use.")
    print("  Usage:")
    print("    To get help:")
    print("         my_program.py -h")
    print("    To find the radius of a circle:")
    print("         my_program.py -r")
    print("    To find the common divisors of two numbers:")
    print("         my_program.py -d")
    print("    To turn a decimal into a binary number:")
    print("         my_program.py -b keyfile inputfile outputfile")
def print_error():
    print("ERROR: Invalid command line arguments!")

import sys

if len(sys.argv)==2 and sys.argv[1]=='-h': # allows for two arguments with one of them having to be -h and calls the instructions function
    print_instructions()
    
elif len(sys.argv)==2 and sys.argv[1]=='-r': # allows for two arguments with one of them having to be -r
        radius=float(input("Please enter the radius of your circle: "))
        if radius >=0:
            A=3.14*radius**2
            print("The area of your circle is: ", A)

elif len(sys.argv)==2 and sys.argv[1]=='-d': # allows for two arguments with one of them having to be -d
        n=0
        div1=int(input("Please enter the first number: "))
        div2=int(input("Please enter the second number: "))
        for i in range(1, min(div1, div2)+1): 
            if div1%i==div2%i==0: 
                n+=1
        print(n)

elif len(sys.argv)==2 and sys.argv[1]=='-b': # allows for two arguments with one of them having to be -b
   
        number = int(input("Enter any whole number: "))
        print("Equivalent Binary Number: ", bin(number))


else:
    print_error()
    print_instructions()