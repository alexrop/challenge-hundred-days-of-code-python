# Day 7/100
# Hangman Game - Optimized Version

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
f.setFont(font='gothic')  # Use `f.getFonts()` to list available fonts

welcome_message = f.renderText('Hangman\nChilean slang')
list_of_words = [
    "Altiro", "Bacan", "Cachai", "Carrete", "Fome", "Cuatico", "Copete", "Guagua", "Pelambre", "Porfiado",
    "Choro", "Po", "Pololear", "Luca", "Quiltro", "Cabro", "Chamba", "Flaite", "Pegote", "Apitutado",
    "Amasanderia", "Pantruca", "Completo", "Pebre", "Empanada", "Porotos", "Chancho", "Choclo", "Chirimoya", "Mote",
    "Paila", "Cochayuyo", "Churrete", "Chispeza", "Jote", "Picado", "Tacano", "Pega", "Yapo", "Alhaja",
    "Piola", "Pelado", "Chato", "Nono", "Chascon", "Lolo", "Copucha", "Zancudo", "Guaren", "Patiperro"
]

################################################################################
# 2.- Functions
################################################################################
def generate_random_word(words: list) -> str:
    '''Returns a random word based on an input list'''
    return random.choice(words)

def ask_for_user_letter() -> str:
    '''Prompts user to input a valid single alphabetical letter'''
    while True:
        letter = input('Guess a letter: ').lower()
        if len(letter) == 1 and letter.isalpha():
            return letter
        print("Invalid input. Please enter a single letter.")

def generate_word_blank_spaces(word: str, correct_letters: list) -> str:
    '''Displays the current known word with blanks for unknown letters'''
    return ''.join([char if char in correct_letters else '_' for char in word])

def generate_hanging_draws(lives: int) -> None:
    '''Displays the hangman drawing based on remaining lives'''
    drawings = [
        """  
============
YOUR DEAD ☠
============
        """,
        """  
+---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
        """,
        """  
+---+
 |   |
 O   |
/|\  |
/    |
     |
=========
        """,
        """  
+---+
 |   |
 O   |
/|\  |
     |
     |
=========
        """,
        """  
+---+
 |   |
 O   |
/|   |
     |
     |
=========
        """,
        """  
+---+
 |   |
 O   |
 |   |
     |
     |
=========
        """,
        """  
+---+
 |   |
     |
     |
     |
     |
=========
        """
    ]
    print(drawings[lives])

################################################################################
# 3.- Main Game Function
################################################################################
def run(total_lives: int = 6) -> None:
    '''Main function to run the hangman game'''
    print(welcome_message)

    word_to_guess = unidecode(generate_random_word(list_of_words).lower())
    unique_letters = set(word_to_guess)
    correct_letters = []
    lives = total_lives

    while True:
        word_display = generate_word_blank_spaces(word_to_guess, correct_letters)
        print(f"\nWord to guess: {word_display}")
        user_letter = ask_for_user_letter()

        if user_letter in unique_letters and user_letter not in correct_letters:
            correct_letters.append(user_letter)
            print("Correct!")
        else:
            if user_letter not in unique_letters:
                print(f"You guessed '{user_letter}', that's not in the word.")
            else:
                print(f"You already guessed '{user_letter}'.")
            lives -= 1

        generate_hanging_draws(lives)
        print(f"**************************** {lives}/{total_lives} LIVES LEFT ****************************")

        if set(correct_letters) == unique_letters:
            print(f"\n🎉 YOU WIN! The word was: {word_to_guess.upper()} 🎉")
            break

        if lives == 0:
            print(f"\n😢 YOU LOSE. The word was: {word_to_guess.upper()} 😢")
            break

################################################################################
# 4.- Execute logic
################################################################################
if __name__ == "__main__":
    run(total_lives=6)