# %%
import random
word_list = [i for i in list((open('1-1000.txt','r').read()).split("\n")) if len(i)>2]

# %%

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))
    
    def check_guess(self, guess):

        guess = guess.lower()
        self.list_of_guesses.append(guess)

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)-1):
                    if guess == self.word[i]:
                        self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} left.")
        
             

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if not ((len(guess) == 1) and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

                
        # 

# %%
Hangman(word_list).ask_for_input()


# %%
