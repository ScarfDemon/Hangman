# %%
import random
# %%

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list #list of words random word will be chosen from
        self.num_lives = num_lives #number of lives left
        self.word = random.choice(word_list) #random word for guessing- chosen from word list
        self.word_guessed = ['_']*len(self.word) #existing state of guessed word where underscore is unguessed character; and letter is guessed character
        self.list_of_guesses = [] #list of every guess made
        self.unique_letters_left = list(set(self.word)) # -1 unique letters when letter guessed correctly- so that hint can choose random letter remaining to reveal
        self.num_letters = len(set(self.word)) #number of unique letters = number of correct guesses (incl hints)
    
    def check_guess(self, guess):

        guess = guess.lower()
        self.list_of_guesses.append(guess) #add guess to list of guesses

        if guess in self.word: #if guessed letter is in the word
            print(f"Good guess! {guess} is in the word.")
            
            for i in range(len(self.word)):
                    if guess == self.word[i]: #if guessed letter is the ith character in the word
                        self.word_guessed[i] = guess #replace the ith '_' with the letter 
            
            self.num_letters -= 1 #number of unique letters in the word left to guess -1; (see play_game) if > 1, continue game and ask for input
            self.unique_letters_left.remove(guess) #remove letter from unique_letters_left- adjusted if hints needed

        else:
            self.num_lives -= 1 #incorrectly guessed reduce lives by 1
            print(f"Sorry, {guess} is not in the word.")
            if self.num_lives == 1: #print you have x lives/life left
                life_s = 'life'
            else:
                life_s = 'lives'
            print(f"You have {self.num_lives} {life_s} left.")
        
        print('  '.join(self.word_guessed)) #prints word guessed so far but without the ['']
        
             

    def ask_for_input(self):
        while True: #loop until a valid input (single letter, asking guessed letters, hint)
            guess = input("\n Please guess a letter: ").lower()
            if guess in self.list_of_guesses: 
                print("You already tried that letter!")
                continue #letter guessed shouldn't already be in list_of_guesses
            elif 'hint' in guess: #hint input hint method
                self.hint()
                break
            elif ('letter' in guess) or ('guess' in guess): #if I ask eg What letters have I guessed?
                print(set(self.list_of_guesses) if len(self.list_of_guesses)>0 else None) # print every letter I've guessed, if no letters guessed, print None
            elif not ((len(guess) == 1) and guess.isalpha()): #guessed letter must be single alphabetical character
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue 
            else:
                self.list_of_guesses.append(guess) #if letter guess is valid, add to list_of_guesses
                self.check_guess(guess) #check_guess method to check if guessed letter is in word
                break
    
    def hint(self):
        hint_letter = random.choice(list(set(self.unique_letters_left))) #out of the remaining letters in the word to be guessed, choose random letter
        print(f'Hint letter: {hint_letter}')
        for i in range(len(self.word)):
            if hint_letter == self.word[i]: # if the chosen letter (for hint) is the ith character of the word
                self.word_guessed[i] = hint_letter #replace the ith character of the word_guessed (which should be '_') with the hint letter
        self.num_letters -= 1 #number of unique letters in the word left to guess -1; (see play_game) if > 1, continue game and ask for input
        self.unique_letters_left.remove(hint_letter)
        print('  '.join(self.word_guessed)) #print new state of word_guessed (with the hint letters filled in)


# %%
def play_game(word_list):
    game = Hangman(word_list, num_lives=10) #instance of Hangman game
    print('\n','  '.join(game.word_guessed)) #initial state of word_guessed (underscores length of word)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            print(f'The answer was {game.word}')
            break
        elif game.num_letters > 0: #if there are still unique letters left to guess (>0) keep asking for input
            game.ask_for_input()
        else: #if lives is not zero and all letters in word has been guessed (num_letters = 0), you have won
            print('Congratulations. You won the game!')
            break

# %%
list_of_words = [i for i in list((open('1-1000.txt','r').read()).split("\n")) if len(i)>2]
play_game(list_of_words)

# %%
