# %%
import random
word_list = [i for i in list((open('1-1000.txt','r').read()).split("\n")) if len(i)>2]

# %%

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.unique_letters = set([i for i in self.word])
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = ['a']
        self.num_letters = len(set(self.word))
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            #guess = input("Please enter another letter: ") 
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            #guess = input("Please enter a letter: ")  

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

        #         for i in range(len(self.word)-1):
        #             if self.guess == self.word[i]:
        #                 self.word[i] = self.guess
        #                 self.unique_letters.remove(self.guess)
        # 

# %%
Hangman(word_list).ask_for_input()


# %%
