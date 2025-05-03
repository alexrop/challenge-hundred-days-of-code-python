# Day 7/100
# Create a program for playing "The Hangman" game
# All documentation of this game is here: https://en.wikipedia.org/wiki/Hangman_(game)
# Also here is a demo: https://hangmanwordgame.com/?fca=1&success=0#/

################################################################################
# 0.- Libraries
################################################################################
import random
from pyfiglet import Figlet
from unidecode import unidecode

################################################################################
# 1.- Parameters
################################################################################
f = Figlet()
f.setFont(font='gothic') # print(f.getFonts()) -> to list all fonts

welcome_message = f.renderText('Hangman\nChilean slang')
list_of_words = [
    "Altiro", "Bacan", "Cachai", "Carrete", "Fome", "Cuatico", "Copete", "Guagua", "Pelambre", "Porfiado",
    "Choro", "Po", "Pololear", "Luca", "Quiltro", "Cabro", "Chamba", "Flaite", "Pegote", "Apitutado",
    "Amasanderia", "Pantruca", "Completo", "Pebre", "Empanada", "Porotos", "Chancho", "Choclo", "Chirimoya", "Mote",
    "Paila", "Cochayuyo", "Churrete", "Chispeza", "Jote", "Picado", "Tacano", "Pega", "Yapo", "Alhaja",
    "Piola", "Pelado", "Chato", "Nono", "Chascon", "Lolo", "Copucha", "Zancudo", "Guaren", "Patiperro"]

################################################################################
# 2.- Functions
################################################################################
def generate_random_word(words:list) -> str:
    '''Returns a random word based on an input list'''
    return random.choice(words)       

def ask_for_user_letter() -> str:
    '''Function that ask for a input letter to the user'''
    letter = input('Guess a letter: ').lower()
    return letter

def store_correct_letters(letter:str, word:str, correct_letters:list=[]) -> list:
    '''Returns a list of correct letters based on user input'''
    word_list = list(word)
    if letter in set(word_list):
        correct_letters.append(letter)
    
    return correct_letters

def generate_word_blank_spaces(word:str, correct_letters:list=[]) -> str:
    '''Function that display all missing spaces based on correct answers'''
    blank_spaces_list = list('_' * len(word))

    if len(correct_letters)!=0:
        for idx,letter in enumerate(word):
            if letter in correct_letters:
                blank_spaces_list[idx] = letter

    return ''.join(blank_spaces_list)  

def generate_hanging_draws(lives:int)->str:
    '''Plotting hangman progress images'''
    if lives==6:
        draw =  """  
    +---+
    |   |
        |
        |
        |
        |
    =========
                """
        print(draw)

    elif lives == 5:
        draw =  """  
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
                """
        print(draw)

    elif lives == 4:
        draw =  """  
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
                """
        print(draw)

    elif lives == 3:
        draw =  """  
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
                """
        print(draw)

    elif lives == 2:
        draw =  """  
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
                """
        print(draw)

    elif lives == 1:
        draw =  """  
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
                """
        print(draw)

    elif lives == 0:
        draw = """  
============
YOUR DEAD ☠
============
               """
        print(draw)

def run(total_lives:int = 6) -> None:
    '''Function that executes all game'''
    print(welcome_message)

    word_to_guess = unidecode(generate_random_word(list_of_words).lower())
    lives = total_lives
    missing_letters = len(set(word_to_guess))
    correct_letters = []
    game_on = True

    while game_on:
        word_blank_spaces = generate_word_blank_spaces(word_to_guess, correct_letters)
        print(f'\nWord to guess: {word_blank_spaces}')    
        user_letter = ask_for_user_letter()
        
        if user_letter in set(word_to_guess):
            correct_letters.append(user_letter)
            missing_letters-=1

            generate_hanging_draws(lives)
            print(f"****************************{lives}/{total_lives} LIVES LEFT****************************")

            if missing_letters==0:
                print(f"\n***********************YOU WIN 🎉!! THE WORD WAS {word_to_guess.upper()} **********************")
                game_on=False

        else:
            lives -= 1
            if lives > 0:
                print(f"You guessed '{user_letter}', that's not in the word. You lose a life.")
                generate_hanging_draws(lives)
                print(f"****************************{lives}/{total_lives} LIVES LEFT****************************")
            else:
                generate_hanging_draws(lives)
                print(f"\n***********************THE WORD WAS '{word_to_guess.upper()}'. YOU LOSE 😢**********************")
                game_on=False

if __name__ == "__main__":
    run(total_lives=6)