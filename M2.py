# %%
import random

# %% # Task 1- make word list
word_list = ['Loquat', 'Banana', 'Mango', 'Persimmon', 'Lychee']
print(word_list)

# %% # Task 2- use random choice
word = random.choice(word_list)
print(word)
# %% # Task 3- input guess letter

guess = input("Please input a single letter: ")



# %% Task 4- check input is a single letter

if (len(guess) == 1) and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# %%
