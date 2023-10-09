import random
word_list = ["apple", "cherry", "melon", "grape", "banana"]
word = random.choice(word_list)
print(word)

def ask_for_input():
    looper = True    
    while looper == True:
        guess = input("Please enter a single letter!")
        if len(guess) == 1 and guess.isalpha() == True:
            print("Good guess!")
            looper = False
        else:
            print("Oops! That is not a valid input.")
    check_guess(guess)
    
def check_guess(guess):
    guess = guess.lower()   
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()