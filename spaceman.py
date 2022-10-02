from ast import Return
import random

#SECTION A - GENERATE A WORD RANDOMLY
def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word
#---------------------------------


#RANDOMLY SELECT WORD

secret_word = load_word()

#---------------------

letters_to_guess = list(secret_word)

#SECTION B - Formatting output with '-' for letters not yet guessed: 
display = ''
for characters in letters_to_guess:
    display += '-'
display_list = list(display)
#---------------------------------------



#SECTION C - Counting occurences of letters in the word to be guessed, so that if there are 2 occurences 
# in the same word, player doesn't have to guess twice:
length = len(letters_to_guess)

def countOccurences (letter):
    letters_to_guess = list(secret_word)
    return letters_to_guess.count(letter)

#----------------------------------------


#Function that takes the guessed letter and adds it in the response array:
def replace(letter): 
    counter = 0
    occurences = countOccurences(letter)
    while counter < occurences:
        index = letters_to_guess.index(letter)
        display_list[index] = letter
        letters_to_guess[index] = '-'
        counter += 1
    return occurences

#SECTION D - MAIN LOGIC OF THE GAME: While loop for the 7 guesses. 
count = 7 
score = 0
print('A word has been selected.')
print(display_list)
while count >= 0:
    if count == 0:
        print(f'sorry, you are out of guesses!\nThe secret word was "{secret_word}"')
        break
    elif(count > 0):    
        guess = input('Please guess a letter: ')
        if guess in letters_to_guess:
            print("Good guess!")
            replace(guess)
            increment_score = countOccurences(guess)
            score += increment_score
            print(f'score {score}/{len(letters_to_guess)}')
            if score == len(letters_to_guess):
                print('CONGRATULATION, you guessed the word!')
                break
        else:
            print(f'{guess} is NOT in the word')
            print(f'score {score}/{len(letters_to_guess)}')
    print(display_list)
    count -= 1
    print(f'{count} guesses remaing. . .')
