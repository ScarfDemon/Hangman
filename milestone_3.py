# %% Randomised word from list of most common words
import random
word_list = [i for i in list((open('1-1000.txt','r').read()).split("\n")) if len(i)>2]
word = random.choice(word_list)
print(word)

# %% #Task 1- iteratively check if input is a valid guess

def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")
        if (len(guess) == 1) and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
    check_guess(guess)

# %% Task 2- Check whether the guess is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        guess = input("Please enter another letter: ") 
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        guess = input("Please enter a letter: ")  

# %%

ask_for_input()

# %%

