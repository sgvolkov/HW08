# After you have gotten Version 0 working, you can proceed to implement this slightly more advanced version.

# usage: python mimsmind1.py [length]
# Once again, the program generates a random number with number of digits equal to length. If the command line argument length 
#is not provided, the default value is 3. This means that, by default, the random number is in the range of 000 and 999. 

# In this version, the program will establish a maximum number of rounds, maxrounds, equal to (2^length) + length. For example, 
#if length = 3, then maxrounds = 11.

# Then, the program prompts the user to type in a guess, informing the user of the number of digits expected. The program will 
#then read the user input, and provide 'bulls and cows' feedback to the user. A matching digit in the correct position will 
#result in a 'bull', while a matching digit in the wrong position will result in a 'cow'. For example, if the correct answer is 
#'123', and the guess is '324', then the feedback will be one bull (for the digit '2') and one cow (for the digit '3'). 
#More examples are provided below.

# At each round, if the user guess is incorrect and maxrounds is not yet reached, the program should increment the 
#counter for round and issue a new prompt for user input. Otherwise, the program should print a congratulatory or an 
#apologetic message with the number of guesses made, and terminate the game.



# Example 1: (solution is '123')

# %% python mimsmind1.py

# Let's play the mimsmind1 game. You have 11 guesses.

# Guess a 3-digit number: 789

# 0 bull(s), 0 cow(s). Try again: 891

# 0 bull(s), 1 cow(s). Try again: 189

# 1 bull(s), 0 cow(s). Try again: 135

# 1 bull(s), 1 cow(s). Try again: 111

# 1 bull(s), 0 cow(s). Try again: 132

# 1 bull(s), 2 cow(s). Try again: 125

# 2 bull(s), 0 cow(s). Try again: 123

# Congratulations. You guessed the correct number in 8 tries.

# %%

# Example 2: (solution is '007')

# %% python mimsmind1.py

# Let's play the mimsmind1 game. You have 11 guesses.

# Guess a 3-digit number: xyz

# Invalid input. Try again: 1

# Invalid input. Try again: 012

# 1 bull(s), 0 cow(s). Try again: 010

# 1 bull(s), 1 cow(s). Try again: 100

# 1 bull(s), 1 cow(s). Try again: 700

# 1 bull(s), 2 cow(s). Try again: 007

# Congratulations. You guessed the correct number in 5 tries.

# %%

# Example 3: (solution is '8')

# %% python mimsmind1.py 1

# Let's play the mimsmind1 game. You have 3 guesses.

# Guess a 1-digit number: 0

# 0 bull(s), 0 cow(s). Try again: 1

# 0 bull(s), 0 cow(s). Try again: 2

# Sorry. You did not guess the number in 3 tries. The correct number is 8.

# %%

import sys
import random

# Body   

def get_length(): # gets the length or sets the default.
    if len(sys.argv) == 2:
        length = sys.argv[1]
    else:
        length = 3
    return length  # this is a string. keep in mind it may need to be an int.

def gen_random1(length):
    number = ""
    for n in range(int(length)): #the loop will run this many times, for the amount of digits 
            number += str(random.randint(0,9))

def get_maxrounds(length):
    length = int(length)
    maxrounds = 2**length + length

def get_initial_guess(length):
    guess = int(raw_input('\nGuess a {0}-digit number: '.format(length)))
    guess_count = 1
    return guess, guess_count

def provide_feedback(guess, rand_num, guess_count):
    while True:
        if guess == rand_num:
            print("\nCongratulations. You guess the correct number in {0} tries." .format(guess_count))
            break
        cows = 0
        bulls = 0
        bull_idx = []
        guess = str(guess)

        #cycle through every digit in guess
        #increment bulls if the digit matches the place of rand_num
        #and add to bull_idx. Else, cycle through every digit in rand_num and 
        #if the index of that digit is not in bull_idx and the digit equals
        # a guess digit, it's a cow.
        for n, digit in enumerate(guess):
            if digit == rand_num[n]:
                bulls += 1
                bull_ix.append(n)  # removing this bull from consideration
            else:
                for n, x in enumerate(rand_num):
                    if n not in bull_idx:
                        if digit == x:
                            cows += 1
        print cows, bulls
        return

        guess_count += 1


################################################################################
def main():

    length = get_length() #variables are called here
    rand_num = gen_random1(length)
    maxrounds = get_maxrounds(length)
    guess, guess_count = get_initial_guess(length)
    provide_feedback(guess, rand_num, guess_count)

if __name__ == '__main__':
    main()
