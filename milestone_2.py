# %%
import random

# %% # Task 1- make word list
word_list = ['Loquat', 'Banana', 'Mango', 'Persimmon', 'Lychee']
print(word_list)

# %% # Task 2- use random choice
word = random.choice(word_list)
wordl = word.lower()
print(word)
# %%

guess = str(input("Please input a single letter: ")).lower()

# %%
