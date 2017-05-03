'''
Let us play Hangman!
'''
import sys
import random
import re

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

def create_dashes(word):

    word_only_dashes = []

    for letter in word:
        # Don't hide hyphens
        if letter == '-':
            word_only_dashes += '-'
        else:
            word_only_dashes += '_'

    return word_only_dashes


def pick_word(file_name):
    #This function will select a random word from a text document
    line_number = None
    stop_number = None

    #Select a random integer to pick from the file
    try:
        #stop_number = random.randint(0,(sum(1 for line in open(file_name))) - 1)
        stop_number = 197560
    except:
        sys.exit('Could not obtain a random number integer')

    with open(file_name,'r') as file:
        for num, line in enumerate(file):
            #If the line is equal to the randomly selected number
            if num == stop_number:
                line_number = line.strip()
                line_number = line_number.lower()
            else:
                continue
        return line_number



#def check_letter(word,letter_guess,word_with_dashes,past_guess,misses):
def check_letter(word,letter_guess,dashes,misses,winner):
    letter_pos = []
    new_word = word
    postion = None
    update_dashes = dashes
    misses_update = misses
    lps = None

    for m in re.finditer(letter_guess,new_word):
         lps = m.start()
         letter_pos.append(lps)
         print "letter_pos is",letter_pos

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

def covert_to_string(to_convert):

    final = ""
    for y in to_convert:
        final += y+" "

    return final


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

def main():
    while True:
        enter_game = raw_input("Do you want to play Hangman? Enter Yes or No. ")

        if isinstance(enter_game, str) and (enter_game.lower() == 'yes'):
            print "Yes it is time to play"
            break
        else:
            print "Alright, maybe later"
            exit()
    #file_name = raw_input("Enter in valid filename of text document you want to pull words from: ")
    file_name = 'random_word.txt'
    #Calling Function
    word = pick_word(file_name)
    print word
    dashes = create_dashes(word)

    print "dashes are",dashes

    initial_prompt = covert_to_string(dashes)

    print "Your word is",initial_prompt

    misses = 0
    guessed_letters = []
    testing = dashes
    currnt_prompt = ""
    winner = False

    while True:
        if winner == True and misses<10:
            print "Congragulations, you have won!"
            main()

        elif misses <= 9:

            guessed_letters = get_letter(guessed_letters)


            testing, misses, winner = check_letter(word,guessed_letters[-1], dashes,misses, winner)

            print "Number of misses are", misses,"out of 10"

            currnt_prompt = covert_to_string(testing)


            state = hangman_state(misses)
            print "What you have guessed correctly is",currnt_prompt
            print "Current Hangman State is",state
            print "Letters guessed are",guessed_letters

        elif misses == 10:
            print "Game Over"
            print "What you have guessed correctly was",currnt_prompt
            print "Final Hangman State is",state
            print "Letters guessed were",guessed_letters
            print "The word was",word
            main()
        else:
            print "Something went wrong"
            exit()



if __name__ == "__main__":
	main()
