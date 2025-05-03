import random
from pyfiglet import Figlet
from unidecode import unidecode

class HangmanGame:
    def __init__(self, word_list: list[str], total_lives: int = 6):
        """
        Initialize the Hangman game with a list of words and a number of lives.
        """
        self.word_list = word_list
        self.total_lives = total_lives
        self.lives = total_lives
        self.correct_letters: list[str] = []
        self.word_to_guess = unidecode(random.choice(word_list).lower())
        self.unique_letters = set(self.word_to_guess)
        self._setup_welcome_message()

    def _setup_welcome_message(self):
        """
        Displays a styled welcome message using pyfiglet.
        """
        f = Figlet()
        f.setFont(font='gothic')
        welcome_message = f.renderText('Hangman\nChilean slang')
        print(welcome_message)

    def ask_for_letter(self) -> str:
        """
        Prompts the user to input a single alphabetical letter.
        Retries until valid input is provided.
        """
        while True:
            letter = input('Guess a letter: ').lower()
            if len(letter) == 1 and letter.isalpha():
                return letter
            print("Invalid input. Please enter a single letter.")

    def display_word_progress(self) -> None:
        """
        Prints the current state of the guessed word with underscores for missing letters.
        """
        display = ''.join([char if char in self.correct_letters else '_' for char in self.word_to_guess])
        print(f"\nWord to guess: {display}")

    def draw_hangman(self) -> None:
        """
        Prints the hangman drawing based on remaining lives.
        """
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
        print(drawings[self.lives])

    def process_guess(self, letter: str) -> None:
        """
        Processes the user's guessed letter:
        - Adds to correct letters if it's a new correct guess.
        - Deducts a life if incorrect or already guessed.
        """
        if letter in self.unique_letters and letter not in self.correct_letters:
            self.correct_letters.append(letter)
            print("Correct!")
        else:
            if letter not in self.unique_letters:
                print(f"You guessed '{letter}', that's not in the word.")
            else:
                print(f"You already guessed '{letter}'.")
            self.lives -= 1

    def game_status(self) -> str:
        """
        Returns the current game status:
        - "won" if all unique letters have been guessed.
        - "lost" if no lives are left.
        - "ongoing" otherwise.
        """
        if set(self.correct_letters) == self.unique_letters:
            return "won"
        elif self.lives == 0:
            return "lost"
        return "ongoing"

    def play(self) -> None:
        """
        Main game loop: runs until player wins or loses.
        """
        while True:
            self.display_word_progress()
            letter = self.ask_for_letter()
            self.process_guess(letter)
            self.draw_hangman()
            print(f"**************************** {self.lives}/{self.total_lives} LIVES LEFT ****************************")

            status = self.game_status()
            if status == "won":
                print(f"\n🎉 YOU WIN! The word was: {self.word_to_guess.upper()} 🎉")
                break
            elif status == "lost":
                print(f"\n😢 YOU LOSE. The word was: {self.word_to_guess.upper()} 😢")
                break


if __name__ == "__main__":
    WORDS = [
        "Altiro", "Bacan", "Cachai", "Carrete", "Fome", "Cuatico", "Copete", "Guagua", "Pelambre", "Porfiado",
        "Choro", "Po", "Pololear", "Luca", "Quiltro", "Cabro", "Chamba", "Flaite", "Pegote", "Apitutado",
        "Amasanderia", "Pantruca", "Completo", "Pebre", "Empanada", "Porotos", "Chancho", "Choclo", "Chirimoya", "Mote",
        "Paila", "Cochayuyo", "Churrete", "Chispeza", "Jote", "Picado", "Tacano", "Pega", "Yapo", "Alhaja",
        "Piola", "Pelado", "Chato", "Nono", "Chascon", "Lolo", "Copucha", "Zancudo", "Guaren", "Patiperro"
    ]

    game = HangmanGame(word_list=WORDS, total_lives=6)
    game.play()