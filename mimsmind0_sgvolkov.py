# Version 0: Basic Feedback (High/Low)

# usage: python mimsmind0.py [length]
# In this version, the program generates a random number with number of digits equal to length. 
#If the command line argument length is not provided, the default value is 1. Then, the program 
#prompts the user to type in a guess, informing the user of the number of digits expected. 
#The program will then read the user input, and provide basic feedback to the user. If the guess 
#is correct, the program will print a congratulatory message with the number of guesses made and 
#terminate the game. Otherwise, the program will print a message asking the user to guess a higher 
#or lower number, and prompt the user to type in the next guess.

# Example 0:

# %% python mimsmind0.py

# Let's play the mimsmind0 game.

# Guess a 1-digit number: 3

# Try again. Guess a higher number: 7

# Try again. Guess a lower number: 5

# Congratulations. You guessed the correct number in 3 tries.

# %%


import random

# Body   

nr_correct = random.randrange(1,10)
length1 = len(str(nr_correct))
str_length1 = str(length1)

def number():
    print "Let's play the mimsmind0 game."
    while True:
        try:
            nr = int(raw_input("Guess a " + str_length1 + "-digit number: "))
        except:
            ValueError
            print "That's not a number! Try again"
            continue
        if nr == nr_correct:
            print "Congrats!"
            break
        elif nr > nr_correct:
            print "Too high, try again"
        elif nr < nr_correct:
            print "Too low, try again"

    print 'the right answer was %d' % nr_correct

################################################################################
def main():

    number()

if __name__ == '__main__':
    main()
