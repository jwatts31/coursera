'''
Let us play Hangman!
'''
import sys
import random
import re
import os

#Function hangman_state: that takes the number of misses a user has and gets the correct hangman
#hangman drawing.
#Input:
#miss_count - an integer from 0 to 10 that represents the number of misses a user has
#Output:
#State - a string of the ASCII drawing of hangman based on the number of misses
def hangman_state(miss_count):
    state = ("""
                -----
                |   |
                |
                |
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                |
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                |  -+-
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\\
                |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\\
                |   |
                |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\\
                |   |
                |   |
                |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\\
                |   |
                |   |
                |  |
                |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\\
                |   |
                |   |
                |  |
                |  |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\\
                |   |
                |   |
                |  | |
                |  |
                |
                --------
                """,
                """
                -----
                |   |
                |   0
                | /-+-\\
                |   |
                |   |
                |  | |
                |  | |
                |
                --------
                """)

    return state[miss_count]

#Function create_dashes: take in a string, can have hypens, and subsitutes
#each character in the string for a dash. Hyphens are left as is.
#Input:
#word - a string to covert to dashes. Only alpha and hypens characters are allowed
#Output:
#word_only_dashes - a list containing underscores for each character in the string
def create_dashes(word):

    #Initialize list
    word_only_dashes = []

    for letter in word:
        # Don't hide hyphens
        word_only_dashes += '_' if letter != '-' else letter

    return word_only_dashes

#Function pick_word: input is a file that has a single word per line.
#A random number is selected, which will be used as the line number
#to select a string
#Input:
#file_name - a file containing one word per line
#Output:
#random_word - the randomly selected string from the file
def pick_word(file_name):

    #Initialize variables
    random_word = None
    stop_number = None

    #Select a random integer
    try:
        stop_number = random.randint(0,(sum(1 for line in open(file_name))) - 1)
        #stop_number = 197560
    except:
        sys.exit('Could not obtain a random number integer')

    with open(file_name,'r') as file:
        for num, line in enumerate(file):
            #If the line is equal to the randomly selected number,
            #strip any white space and make the word lower case
            if num == stop_number:
                random_word = line.strip()
                random_word = random_word.lower()
            else:
                #continue to next line
                continue

        return random_word



#Function check_letter: determines if the character that the user guessed is found.
#If the letter or letters are found, the underscore is replaced by that character
#If there are no more udnerscores in the list, the winner flag is set
#If the character guessed is not in the list, the missed counter is incremented by 1
#Input:
#word - a string that the user is trying to guess
#letter_guess - a single alpha character that the user inputed
#dashes - a list of underscores representing each character in word. Some dashes may be replaced by correctly guessed characters
#misses - a integer representing the number of misses the user has
#winner - a boolean true false flag
#Output:
#update_dashes - a list of underscores representing each character in word. Some dashes may be replaced by correctly guessed characters
#misses_update - a integer representing the number of misses the user has
#winner - a boolean true false flag
def check_letter(word,letter_guess,dashes,misses,winner):
    letter_pos = []
    update_dashes = dashes
    misses_update = misses
    lps = None

    for m in re.finditer(letter_guess,word):
         lps = m.start()
         letter_pos.append(lps)

    if not letter_pos:
        misses_update += 1
    else:
        for x in letter_pos:
            print "The letter",letter_guess,"was found in the word"
            update_dashes[x] = letter_guess

            if '_' in update_dashes:
                continue
            else:
                winner = True


    return update_dashes, misses_update, winner

#Function covert_to_string: coverts a list of characters to a string.
#Input:
#to_convert - a list
#Output:
#final_word - a string made created from concatinating each element in the list

def covert_to_string(to_convert):

    final_word = ""
    for y in to_convert:
        final_word += y+" "

    return final_word

#Function get_letter: asks the user to input a single alpha character
#Input:
#guessed_letters - a list of alpha characters already guessed
#Output:
#guessed_letters_new - a list of alpha characters already guessed with the new guessed character at the end
def get_letter(guessed_letters):

    letter_guess = None
    guessed_letters_new = guessed_letters


    while True:
        letter_guess = raw_input("Enter in letter: ")


        if letter_guess.isalpha() == False:
            print "The letter you guessed is not an alphabetic character"
            continue

        elif len(letter_guess) > 1:
            print "You can only enter one letter at a time"
            continue
        elif letter_guess in guessed_letters_new:
            print "You have already guessed this letter"
            continue
        else:
            try:
                letter_guess.lower()
            except:
                sys.exit('Could covert your guess to a lower case')

            guessed_letters_new += letter_guess
            break

    return guessed_letters_new

def new_page():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        enter_game = raw_input("Do you want to play Hangman? Enter Yes or No. ")

        if isinstance(enter_game, str) and (enter_game.lower() == 'yes'):

            print "Yes it is time to play"
            break
        else:
            print "Alright, maybe later"
            exit()

    file_name = raw_input("Enter in valid filename of text document you want to pull words from (Hit enter to use the default file): ")
    if ( len(file_name) < 1 ) : file_name = 'random_word.txt'

    #Calling Function
    word = pick_word(file_name)

    word_with_dashes = create_dashes(word)

    initial_word_to_user = covert_to_string(word_with_dashes)
    new_page()

    print "Your word is",initial_word_to_user,'\n'

    #Initialize variables
    misses = 0
    guessed_letters = []
    current_word_to_user = ""
    winner = False

    while True:
        if winner == True and misses<10:
            print "Congragulations, you have won!",'\n'
            main()

        elif misses <= 9:
            guessed_letters = get_letter(guessed_letters)
            new_page()
            word_with_dashes, misses, winner = check_letter(word,guessed_letters[-1], word_with_dashes,misses, winner)

            current_word_to_user = covert_to_string(word_with_dashes)

            state = hangman_state(misses)

            print "Number of misses are", misses,"out of 10",'\n'
            print "What you have guessed correctly is",current_word_to_user,'\n'
            print "Current Hangman State is",state,'\n'
            print "Letters guessed are",guessed_letters,'\n'



        elif misses == 10:
            new_page()

            print "Game Over",'\n'
            print "What you have guessed correctly was",current_word_to_user,'\n'
            print "Final Hangman State is",state,'\n'
            print "Letters guessed were",guessed_letters,'\n'
            print "The word was",word,'\n'
            main()
        else:
            print "Something went wrong"
            exit()



if __name__ == "__main__":
	main()
