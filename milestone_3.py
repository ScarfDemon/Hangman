# %% #Task 1- iteratively check if input is a valid guess
while True:
    guess = input("Please guess a letter: ")
    if (len(guess) == 1) and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue

# %%
