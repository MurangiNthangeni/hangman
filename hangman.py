import random
import sys


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    character = ""
    random_letter = word[random.randint(0, len(word)-1)]

    for letter in word:
        if random_letter == letter:
            character = character + letter
            continue

        character = character + "_"
    return character
   
# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if char in original_word and char not in answer_word:
        return True
    
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    new_word = ""

    for i in range(len(original_word)):
        if original_word[i] == char:
            new_word = new_word + original_word[i]
            continue

        new_word = new_word + answer_word[i]
        
    return new_word



def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    number_guesses = number_guesses - 1

    if number_guesses == 0:
        print("Sorry, you are out of guesses. The word was:", answer)
        draw_figure(number_guesses)
    else:
        print('Wrong! Number of guesses left: '+str(number_guesses))
        draw_figure(number_guesses)
    
    return number_guesses


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 0:
        print('''/----
|   0
|  /|\\
|   |
|  / \\
_______''')
    elif number_guesses == 1:
        print('''/----
|   0
|  /|\\
|   |
|  
_______''')
    
    elif number_guesses == 2:
        print('''/----
|   0
|   |
|   |
|  
_______''')
  

    elif number_guesses == 3:
        print('''/----
|   0
|
|
|
_______''')
    
    else:
        print('''/----
|
|
|
|
_______ ''')


# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    number_guesses = 5
    print("Guess the word: "+ answer)

    while number_guesses > 0:
        guess = get_user_input()
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
            if answer == word:
                break
        elif guess in ["exit", "quit"]:
            print("Bye!")
            break
        else:
            number_guesses = do_wrong_answer(word, number_guesses)
            
        
    


# TODO: Step 6 - update to get words_file to use from commandline argument
def get_argument():
    if len(sys.argv)>2:
        file_name = sys.argv[1]
        return file_name
    else:
        file_name = 'short_words.txt'
        return file_name
    
if __name__ == "__main__":
    words_file = get_argument()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

