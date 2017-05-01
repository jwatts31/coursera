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
            word_only_dashes += '- '
        else:
            word_only_dashes += '_ '

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

#def play_game():

#def check_letter(word,letter_guess,word_with_dashes,past_guess,misses):
def check_letter(word,letter_guess,dashes,misses):
    letter_pos = []
    new_word = word
    postion = None
    update_dashes = dashes
    misses_update = misses

    for m in re.finditer(letter_guess,new_word):
         lps = m.start()
         letter_pos.append(lps)

    if not letter_pos:
        misses_update += 1
    else:
        for x in letter_pos:
            #print "X is",x
            update_dashes[x] = letter_guess





    return update_dashes, misses_update

def covert_to_string(to_convert):

    final = ""
    for y in to_convert:
        final += y

    return final


#def end_hangman():


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

    initial_prompt = covert_to_string(dashes)

    print "Your word is",initial_prompt

    #picture = hangman_state(6)
    #print word
    #print dashes
    #print "Here is your word: \n" + dashes

    misses = 0
    guessed_letters = []
    testing = dashes

    while True:
        if misses <= 9:
            letter_guess = raw_input("Enter in letter: ")
            letter_guess.lower()
            guessed_letters += letter_guess

            testing, misses = check_letter(word,letter_guess, dashes,misses)

            print "Number of misses are", misses

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
            exit()
        else:
            print "Something went wrong"
            exit()



if __name__ == "__main__":
	main()
