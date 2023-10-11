import random

class Hangman:
    # innitialise the attributes needed for the hangman game
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def ask_for_input(self):
        while True: #keeps the program running infinitely 
            guess = input("Please enter a single letter!")
            if len(guess) != 1 or guess.isalpha() == False: # Checks if the input from the user is valid 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: # checks if the user has already entered this character as a guess
                print("You already tried that letter!")
                print(f"You have guessed {self.list_of_guesses}") 
            else:
                self.list_of_guesses.append(guess) # adds the users input to the list of characters that have been guessed so far (if valid)
                self.check_guess(guess)  # recalls the check_guess method in the loop 
                print(f"You have guessed {self.list_of_guesses}")
    
    def check_guess(self, guess): # checks to see if the users guess is in the selected hangman word
        guess = guess.lower()   
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            listed_word = list(self.word)
            for i in range(len(listed_word)):    
                if guess == listed_word[i]:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    
testing = Hangman(word_list = ["apple", "cherry", "melon", "grape", "banana"], num_lives = 5)
testing.ask_for_input()
