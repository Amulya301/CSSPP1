"""Implementing the cat shell command in python."""
'''The import statement import sys imports the library sys from the python module along with the functions and methods of the library sys.'''
import sys
'''From the lib.helper module we are importing the built-in functions cat and readfile of the lib.helper module into our source code.'''
from lib.helper import cat, readfile
#TEXT is a variable assigned with a none type.
TEXT = None
'''ARG_CNT is a variable assigned with an int value len(sys.argv) -1.len() function takes one argument as input and returns the length of the given input.'''
ARG_CNT = len(sys.argv) - 1
'''if statement is used to check the condition and execute it if the condition is true.Here if ARG_CNT value is 0 then it reads the input using the standard input function stdin and read() function reads the input from the file and stores it in TEXT variable.'''
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
'''The below if statement checks the condition ARG_CNT is equal to 1, if it is satisfied, it executes the first line sys.argv[1] that is it returns the filename and stores it in the variable filename in the form of string. Then it reads the content of the filename variable using readfile function and assigns the output to the TEXT variable in the form of string.'''
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
'''This if statement checks if ARG_CNT>1 or not. If the condition is true it prints the name of the current python file and the given text using print() function.
    print() function prints the specified values to the output screen.'''
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")
'''The print() function is used to print the output to the terminal.In the below print() function it first executes the cat() function which takes one argument, is used to return the contents of the variable TEXT and then prints the contents to the output screen.'''
print(cat(TEXT))

