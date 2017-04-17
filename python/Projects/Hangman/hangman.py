'''
Let us play Hangman!
'''
import sys
import random

#def hangman_state():

def pick_word(file_name):
    #This function will select a random word from a text document
    line_number = None
    stop_number = None

    #Select a random integer to pick from the file
    try:
        stop_number = random.randint(0,(sum(1 for line in open(file_name))) - 1)
    except:
        sys.exit('Could not obtain a random number integer')

    with open(file_name,'r') as file:
        for num, line in enumerate(file):
            #If the line is equal to the randomly selected number
            if num == stop_number:
                line_number = line.strip()
            else:
                continue
        return line_number

#def check_letter():

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




if __name__ == "__main__":
	main()
