# %%
import random

# %% # Task 1- make word list
word_list = ['Loquat', 'Banana', 'Mango', 'Persimmon', 'Lychee']
print(word_list)

# %% # Task 2- use random choice
word = random.choice(word_list)
wordl = word.lower()
print(word)
# %% # Task 3- input guess letter

guess = input("Please input a single letter: ")
guessl = str(guess).lower()



# %%

if (len(guessl) == 1) and guessl.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# %%
