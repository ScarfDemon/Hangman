# %%
import random

# %% # Task 1- make word list
word_list = ['Loquat', 'Banana', 'Mango', 'Persimmon', 'Lychee']
print(word_list)

# %% # Task 2- use random choice
word = random.choice(word_list)
word = word.lower()
print(word)
# %%

guess = input("Please input a single letter: ")
guess = str(guess).lower()

# %%
