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
        if guess in self.word: # Checks if the character the user is currently guessing is in the randomized word
            print(f"Good guess! {guess} is in the word.")
            listed_word = list(self.word) # Variable to turn the randomized word into a list
            for i in range(len(listed_word)):    
                if guess == listed_word[i]: # Checks if the users guess is inside the list made up of the randomized word
                    self.word_guessed[i] = guess # Adds the guess into the list of current correct inputs from the user
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1  # Takes away a life if the user is not correct with their guess
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
    
    def play_game(self):
        while True:
            if self.num_lives == 0:  # Checks whether the user has lost or not
                print("You lost")
                break
            elif self.num_letters > 0: # Checks whether the game should keep continuing or not
                self.ask_for_input()
            else:
                print(f"Congratulations you have won the game, the word was {self.word}") # Checks whether the user has won or not
                break


game = Hangman(word_list = ["apple", "cherry", "melon", "grape", "banana"], num_lives = 5) # Creates the object to run the game
game.play_game()









