# %%
import random
word_list = [i for i in list((open('1-1000.txt','r').read()).split("\n")) if len(i)>2]

# %%

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list #list of words random word will be chosen from
        self.num_lives = num_lives #number of lives left
        self.word = random.choice(word_list) #random word for guessing- chosen from word list
        self.word_guessed = ['_']*len(self.word) #existing state of guessed word where underscore is unguessed character; and letter is guessed character
        self.list_of_guesses = [] #list of every guess made
        self.num_letters = len(set(self.word)) #number of unique letters = number of correct guesses
    
    def check_guess(self, guess):

        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                    if guess == self.word[i]:
                        self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print("You have {s} {l} left.".format(s=self.num_lives, l= 'life' if self.num_lives==1 else 'lives'))
             
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

                

# %%
Hangman(word_list).ask_for_input()


# %%
