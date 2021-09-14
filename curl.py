"""The python code helps to read the command line input for curl method."""
'''The import statement import sys imports the library sys from the python module along with the functions and methods of the library sys.'''
import sys
'''From the lib.helper module we are importing the built-in functions curl of the lib.helper module into our source code.'''
from lib.helper import curl
# The URL variable is assigned with a none type value.
URL = None
'''ARG_CNT is a variable assigned with an int value len(sys.argv) -1.len() function takes one argument as input and returns the length of the given input.'''
ARG_CNT = len(sys.argv) - 1
'''The below conditional statement ‘if’ checks if ARG_CNT is not equal to 1 if it is satisfied, it prints the output as Usage: curl[URL].. using  print() function.'''
if ARG_CNT != 1:
    print('Usage: curl [URL]...')
'''The below if conditional statement checks whether ARG_CNT is equal to 1, if satisfied it then executes the statements in the conditional.The first statement sys.argv[1] returns the url and stores it in a variable URL in the form of string.'''
if ARG_CNT == 1:
    URL = sys.argv[1]
    '''This is a nested if statement, there can be multiple if statements inside the main if statement.
    The below statement checks if http is present or not in the first 5 positions of the string of URL variable, if it is not present in the string it appends the http:// pattern to the URL variable and assigns the output to the URL variable again.'''
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    #This function first curls the url and prints the html code of the specified url website using curl() function and it takes 1 argument as input and then prints the output to the screen using print() function.
    print(curl(URL))
