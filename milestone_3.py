# %%
import random
word_list = [i for i in list((open('1-1000.txt','r').read()).split("\n")) if len(i)>2]
word = random.choice(word_list)
print(word)
# %% #Task 1- iteratively check if input is a valid guess
while True:
    guess = input("Please guess a letter: ")
    if (len(guess) == 1) and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue

# %%

if guess.lower() in word.lower():
    print(f"Good guess! {guess} is in the word.")
    guess = input("Please enter another letter: ") 
else:
    print(f"Sorry, {guess} is not in the word. Try again.")
    guess = input("Please enter a letter: ")  
# %%


# %%

