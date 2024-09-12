import random


# Getting users name and greeting users

name = input("What is your name? ")
print("Good Luck !", name)


# Lists of words and choosing a random word
words = ['rainbow', 'computer', 'science', 'programming', 'python',
         'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks',]

word = random.choice(words)

# Prompting user to guess
print("Welcom to word Guessing Game. ")

#initializing Guesses and turns

guesses = ''
turns = 12


while turns > 0:
    failed = 0
    for char in word:
        if char  in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
            
# checking if the user has won

    if failed == 0:
        print('')
        print("Cogratulations You Win, the word is: ", word)
        break


    guess = input("guess a character:")
    guesses += guess

    #Handeling incorrect Guesses
    if guess not in word:
        turns -= 1
        print("Wrong Character can not be found or not my choice")
        print("You have", + turns, 'more guesses')
        
    
    if turns == 0:
        print("You Loose")
            