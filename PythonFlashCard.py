##############
##
##  PythonFlashCard.py
##  Chad W. Jennings
##  5 Jan 2016
##
##############

##  This script executes a flash card program on all IndexCard  items from Learn 
#   Python the Hard ##  way.  

#   Flow 
#   1. Define the material to learn in a csv with two columns
#       Command or String or Punctuation       ,     Description
#   3. Load the file 
#   4. Pick a random row from the array.
#   5. Print the description and let the user input the command.
#   6. if the user asks for help then print the command and the 
#       description
#   7.  Keep going till the user quits
#   Possible extensions
#       Keep score
#       verify that randint provides a uniform distribution
#       Host this on a website
#       Keep analytics on 
#           which ones the person gets right and which ones they don't 
#            get right.
#   Obvious extensions
#       Add all the "index card items" from Learning Python the Hard Way
#           to the library file, FlashCardLibrary.txt

# Import necessary methods
from random import randint

# Define a function to count the number of lines in the file
# thank you Silent Ghost
#   http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1 
    f.close

# Read the file into an array of lines called library
f = open('FlashCardLibrary.txt','r')
library = f.readlines()     
f.close                        

# Set parameters and flags necessary for the while loop and start the game
numRows = file_len('FlashCardLibrary.txt') 
continueFlag = True
rightAnswer = False
firstTime = True

print "\n **********  Thanks for Playing **********"
print "\nEnter the answer, type \"quit game\" to end or \"help me\" for the answer:  " 

while continueFlag:
    # if they got the right answer last time through or if this is the
    # first time then pick a new row and split it into answer and prompt
    if rightAnswer or firstTime:
        rowNum = (randint(2,numRows))       # Skip row 1 because the column labels are there
                                            # randint creates a uniform distribution so all
                                            # rows have an equal chance every time.

        #print "numRows %d and the row # %d" % (numRows, rowNum)
        line = library[rowNum-1]            # Selects the rowNum-1 th row in the library
                                            # library index starts at 0. rowNum starts at 1
        answer,prompt = line.split(',')     # Split line into two portions
        answer = answer.strip()             # Strip off whitespaces
        prompt = prompt.strip()        
        firstTime = False
    # else keep the same prompt and answer

    print "\n", prompt, "\n"                # Print the question

    # Get and Process the answer
    input = raw_input()                     
    if answer in input:                     # if they got it right then acknowledge 
        rightAnswer = True                  # and continue
        continueFlag = True                 
        print "Good for you"
    elif "quit" in input:                   # quit if desired
        continueFlag = False
    elif "help" in input:                   # help 'em out if requested
        print line
        rightAnswer = False
    else:
        print "Try Again"                   # keep going till you get the right answer
        rightAnswer = False   

print "\n **********  Thanks for Playing  **********\n"








