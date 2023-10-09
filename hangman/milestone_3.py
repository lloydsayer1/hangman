looper = True

while looper == True:
    guess = input("Please enter a single letter!")
    if len(guess) == 1 and guess.isalpha() == True:
        print("Good guess!")
        looper = False
    else:
        print("Oops! That is not a valid input.")