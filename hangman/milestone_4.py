import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def ask_for_input(self):   
        while True:
            guess = input("Please enter a single letter!")
            if len(guess) == 1 and guess.isalpha() == True:
                print("Good guess!")
                break
            else:
                print("Oops! That is not a valid input.")
        self.check_guess(guess)
    
    def check_guess(self, guess):
        guess = guess.lower()   
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    
testing = Hangman(word_list = ["apple", "cherry", "melon", "grape", "banana"], num_lives = 5)
testing.ask_for_input()
