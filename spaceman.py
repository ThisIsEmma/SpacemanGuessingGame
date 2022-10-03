from ast import Return
import random

#load list of word using part of the startup code 
def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

#Read spaceman ASCII art
def load_spaceman():
    f = open('spaceman.txt', 'r')
    spaceman_list = f.read()
    f.close()
    return spaceman_list

#STRETCH Challenge - print a Spaceman ASCI art with each incorrect guesses 
def print_spaceman(count):
    list = load_spaceman()
    if count == 0:
        print(f"\033[1;37;40m White {list[0:5172]} \033[0m")
    elif count == 1:
        print(f"\033[1;37;40m White {list[738:5172]} \033[0m")
    elif count == 2:
        print(f"\033[1;37;40m White {list[1477:5172]} \033[0m")
    elif count == 3:
        print(f"\033[1;37;40m White {list[2216:5172]} \033[0m")
    elif count == 4:
        print(f"\033[1;37;40m White {list[2955:5172]} \033[0m")
    elif count == 5:
        print(f"\033[1;37;40m White {list[3694:5172]} \033[0m")
    elif count == 6:
        print(f"\033[1;37;40m White {list[4433:5172]} \033[0m")


#RANDOMLY select a word and STORE it as a list 
secret_word = load_word()
print(secret_word) 
letters_to_guess = list(secret_word)


#Placeholder to contain '-' for letters not yet guessed: 
def generate_placeholder(letters_to_guess):
    display = ''
    for characters in letters_to_guess:
        display += '-'
    placeholder = list(display)
    return placeholder


#Counting occurences of letters in the word to be guessed, so that if there are 2 occurences or more
# in the same word, player doesn't have to guess twice:
length = len(letters_to_guess)
def countOccurences (letter):
    letters_to_guess = list(secret_word)
    return letters_to_guess.count(letter)



#Add letter in the placeholder (if letter is part of the secret word):
def replace(letter, letters_to_guess, placeholder): 
    counter = 0
    occurences = countOccurences(letter)
    while counter < occurences:
        index = letters_to_guess.index(letter)
        placeholder[index] = letter
        letters_to_guess[index] = '-'
        counter += 1
    return occurences

#Check if letter has already been guessed: 
def is_already_guessed(letter, placeholder):
    if letter in placeholder:
        return True
    else:
        return False

#STRETCH CHALLENGE - Validate input (individual letters only)
def prompt_for_letter():
    user_input = input('Please enter a letter: ')
    while(len(user_input)>1):
        print('Individual letters only')
        user_input = input('Please enter a letter: ')
    return user_input



#Main logic of the game: While loop for the 7 guesses. 
count = 6 
score = 0
play = True
print('A word has been selected.')
placeholder = generate_placeholder(letters_to_guess)
print(f'\n{placeholder}\n')
while count >= 0 and play == True:
    if count == 0:
        print(f'\033[1;31;40m SORRY YOU ARE OUT OF GUESSES !\nThe secret word was "{secret_word}"\033[0m')
        print_spaceman(0)
        print('\nWant to play again ? (y for YES | type any key for NO)')
        play_again = prompt_for_letter()
        if play_again == 'y': #STRETCH Challenge - Prompt the player to play again. 
            play = True
            count = 6
            score = 0
            print('\n\nAnother word has been selected.')
            secret_word = load_word()
            print(secret_word) 
            letters_to_guess = list(secret_word)
            placeholder = generate_placeholder(letters_to_guess)
            print(f'\n{placeholder}\n')
            continue
        else:
            print('Thank you for playing!')
            play = False
        break
    elif(count > 0):  
        guess = prompt_for_letter()
        if is_already_guessed(guess, placeholder): #STRETCH CHALLENGE - check if letter has already been guessed and don’t have it count as an incorrect guess
            print(f'\033[1;37;40m I promise you this word has no more "{guess}" left to guess...\033[0m')
        else:
            if guess in letters_to_guess:	
                print("\033[1;32;40m GOOD GUESS ! \033[0m")
                replace(guess, letters_to_guess, placeholder)
                increment_score_by = countOccurences(guess)
                score += increment_score_by
                print(f'\033[1;37;40m score {score}/{len(letters_to_guess)}\033[0m')
                if score == len(letters_to_guess):
                    print(placeholder)
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
                        letters_to_guess = list(secret_word)
                        placeholder = generate_placeholder(letters_to_guess)
                        print(placeholder)
                        continue
                    else:
                        print('Thank you for playing!')
                        play = False
                    break
            else:
                print(f'\033[1;31;40m INCORRECT GUESS. {count} guesses remaining. . . \033[0m')
                print(f'\033[1;37;40m score {score}/{len(letters_to_guess)}\033[0m')
                print_spaceman(count)
                count -= 1
    print(f'\n{placeholder}\n')
