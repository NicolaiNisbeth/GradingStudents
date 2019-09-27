import os.path
import re

def inputFilename():
    # INPUTFILENAME Prompts user to input a filename
    #
    # Usage: filename = inputFilename(prompt) Displays prompt and asks user to 
    # input a filename. Repeats until user inputs a filename of an existing 
    # file.
    #
    # Author: From "Solution (Bacteria data analysis)" made by Mikkel N. Schmidt
    
    while True:
        filename = input("You may now enter your filename: ")
        if os.path.isfile(filename) and re.search('\.csv', filename):
            break
        print("File \"{:s}\" does not exist. Please input a valid filename.".format(filename))
    return filename