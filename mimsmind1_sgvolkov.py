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

import random
def number():
    digits = '123456789'
    size = 3
    secret_number = ''.join(random.sample(digits,size))
    secret_number_str = str(secret_number)
    len_secret = len(str(secret_number))
    str_len_secret = str(len_secret)
    maxrounds = (2**(len_secret)) + (len_secret)
    #print chosen # Debug
    print secret_number
    print "\nLet's play the mimsmind1 game. You have " + str(maxrounds) +" guesses."
    guesses = 0
    while True:
        guesses += 1
        guesses_left = maxrounds - guesses
        while True:
            # get a good guess
            guess = raw_input('\nGuess a %i -digit number: ' % size).strip()
            if len(guess) == size and \
               all(char in digits for char in guess) \
               and len(set(guess)) == size:
                break
            print "Problem, try again. You have %i guesses left" % guesses_left
        if guess == secret_number:
            print '\nCongratulations you guessed correctly in',guesses,'attempts'
            break
        if guesses == maxrounds:
            print "Sorry. You did not guess the number in " + str_len_secret + " tries. The correct number is " + secret_number_str
        bulls = cows = 0
        for i in range(size):
            if guess[i] == secret_number[i]:
                bulls += 1
            elif guess[i] in secret_number:
                cows += 1
        print ' %i Bulls\n %i Cows' % (bulls, cows)
        print "Try again. You have " + str(guesses_left) + " guesses left: "

################################################################################
def main():

    number()

if __name__ == '__main__':
    main()
