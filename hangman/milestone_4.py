import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def ask_for_input(self):

        while True:
            guess = input("Please enter a single letter!")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                self.list_of_guesses.append(guess)
                print(f"You have guessed {self.list_of_guesses}")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                print(f"You have guessed {self.list_of_guesses}")
    
    def check_guess(self, guess):
        guess = guess.lower()   
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            word_list = list(self.word)
            for i in word_list:
                if guess == word_list[i]:
                    word_list[i] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {num_lives} lives left.")

    
testing = Hangman(word_list = ["apple", "cherry", "melon", "grape", "banana"], num_lives = 5)
testing.ask_for_input()
