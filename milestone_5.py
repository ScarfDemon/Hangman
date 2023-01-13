# %%
import random
# %%

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = []
        self.unique_letters_left = list(set(self.word))
        self.num_letters = len(set(self.word))
    
    def check_guess(self, guess):

        guess = guess.lower()
        self.list_of_guesses.append(guess)

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.unique_letters_left.remove(guess)
            for i in range(len(self.word)):
                    if guess == self.word[i]:
                        self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            if self.num_lives == 1:
                life_s = 'life'
            else:
                life_s = 'lives'
            print(f"You have {self.num_lives} {life_s} left.")
        print(self.word_guessed)
        
             

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ").lower()
            if guess == 'hint':
                self.hint()
            elif not ((len(guess) == 1) and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break
    
    def hint(self):
        hint_letter = random.choice(list(set(self.word)))
        for i in range(len(self.word)):
                if hint_letter == self.word[i]:
                    self.word_guessed[i] = hint_letter
        self.num_letters -= 1
        print(self.word_guessed)


# %%
def play_game(word_list):
    game = Hangman(word_list, num_lives=10)
    print(game.word_guessed)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            print(f'The answer was {game.word}')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

# %%
list_of_words = [i for i in list((open('1-1000.txt','r').read()).split("\n")) if len(i)>2]
play_game(list_of_words)
# %%
