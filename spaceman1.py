import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
  
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    secret_word_list = list(secret_word)
    if sorted(letters_guessed) == sorted(secret_word_list):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    secret_word_list = list(secret_word)
    underscores = ''
    for characters in secret_word_list:
        underscores += '_'
    placeholder = list(underscores)
    
    for secret_letter in secret_word_list:
        for guessed_letter in letters_guessed:
            if  secret_letter == guessed_letter:
                occurences = secret_word_list.count(guessed_letter) 
                if occurences > 1:
                    while occurences > 1:
                        index = secret_word_list.index(guessed_letter)
                        placeholder[index] = guessed_letter
                        secret_word_list[index] = '_'
                        occurences -= 1
                else:
                    index = secret_word_list.index(secret_letter)
                    placeholder[index] = guessed_letter                
    
    return placeholder


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    secret_word_list = list(secret_word)
    if guess in secret_word_list:	
        return True
    else:
        return False


def prompt_for_letter():
    '''
    A function to prompt user for a one letter input, and validate that the input is acceptable (1 letter only)
    Args:
        none
    Returns:
        string: letters and numbers
    '''
    user_input = input('Please enter a letter: ')
    while(len(user_input)>1):
        print('Individual letters only')
        user_input = input('Please enter a letter: ')
    return user_input

def is_already_guessed(guess, letters_guessed):
    '''
    A function to inform user that letter was already guessed (I.e new guess is already existing in the guessed letter list) 
    Args:
        guess (string): individual letter provided by user
        letters_guessed: list of letter already guessed by user 
    Returns:
        Bool: True if guess already exists in letters_guess list; False if it does not.
    '''
    if guess in letters_guessed:
        return True
    else:
        return False

def print_spaceman(count):
    '''
    A function to load a spaceman ASCII arts and output portions of it when the player guesses incorrectly.
    Args:
        count (number): from 0-6, for each count representing the number of incorrect guesses 
    Returns:
        void.
    '''
    f = open('spaceman.txt', 'r')
    spaceman_list = f.read()
    f.close()
    list = spaceman_list
    if count == 0:
        print(f"\033[1;37;40m {list[0:5172]} \033[0m")
    elif count == 1:
        print(f"\033[1;37;40m {list[738:5172]} \033[0m")
    elif count == 2:
        print(f"\033[1;37;40m {list[1477:5172]} \033[0m")
    elif count == 3:
        print(f"\033[1;37;40m {list[2216:5172]} \033[0m")
    elif count == 4:
        print(f"\033[1;37;40m {list[2955:5172]} \033[0m")
    elif count == 5:
        print(f"\033[1;37;40m {list[3694:5172]} \033[0m")
    elif count == 6:
        print(f"\033[1;37;40m {list[4433:5172]} \033[0m")

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec
    print('Welcome to SPACEMAN ! A word has been randomly selected.\n Can you guess the word? one letter at a time')
    
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    #Please see prompt_for_letter() above - Used a function instead to reuse it when asking the player if they want to play again.

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    count = 6
    score = 0
    play = True
    letters_guessed = []
    while count >= 0 and play == True:
        if count == 0:
            print(f'\033[1;31;40m SORRY YOU ARE OUT OF GUESSES !\nThe secret word was "{secret_word}"\033[0m')
            #print_spaceman(0)
            print('\nWant to play again ? (y for YES | type any key for NO)')
            play_again = prompt_for_letter() #recycling prompt_for_letter() as the following if-stmt requires 1 letter input
            if play_again == 'y': 
                play = True
                count = 6
                score = 0
                print('\n\nAnother word has been selected.')
                secret_word = load_word()
                print(secret_word) 
                letters_guessed = []
                print(get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                print('Thank you for playing!')
                play = False
            break
        elif(count > 0):  
            guess = prompt_for_letter()
            if is_already_guessed(guess, letters_guessed) == True:
                print(f'\033[1;37;40m I promise you this word has no more "{guess}" left to guess...\033[0m')
            else: 
                if is_guess_in_word(guess, secret_word) == True:
                    occurences = list(secret_word).count(guess)
                    print("\033[1;32;40m GOOD GUESS ! \033[0m")
                    letters_guessed += (guess * occurences)
                    print(f'Guessed letters so far: {letters_guessed}')
                    print(get_guessed_word(secret_word, letters_guessed))
                    score += occurences
                    print(f'\033[1;37;40m score {score}/{len(list(secret_word))}\033[0m')
    #TODO: show the guessed word so far
                    print(is_word_guessed(secret_word, letters_guessed))
    #TODO: check if the game has been won or lost
                    if (is_word_guessed(secret_word, letters_guessed)) == True:
                        print('\033[1;33;40m CONGRATULATION, you guessed the word!\033[0m')
                        print('\nWant to play again ? (y for YES | type any key for NO)')
                        play_again = prompt_for_letter()
                        if play_again == 'y':
                            play = True
                            count = 6
                            score = 0
                            print('Another word has been selected.')
                            secret_word = load_word()
                            print(secret_word)
                            letters_guessed = []
                            print(get_guessed_word(secret_word, letters_guessed))
                            continue
                        else:
                            print('Thank you for playing!')
                            play = False
                        break
                elif is_guess_in_word(guess, secret_word) == False: 
                    print(f'\033[1;31;40m INCORRECT GUESS. {count} guesses remaining. . . \033[0m')
                    print(f'\033[1;37;40m score {score}/{len(list(secret_word))}\033[0m')
                    print_spaceman(count)
                    count -= 1
                    print(get_guessed_word(secret_word, letters_guessed))
  
    
    
#These function calls that will start the game
secret_word = load_word()
print(secret_word)
spaceman(secret_word)