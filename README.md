# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Steps to hangman game

## Milestone 2
Milestone 2 achieves the first step in creating a hangman game. It generates a random word from a small defined list of words. After asking the user for an input as the guessed letter, an if statement checks if the input is a  single letter of the alphabet, alerting the user if it is an invalid guess.

## Milestone 3
Milestone 3 creates two functions that serve to complete checks: 

    ask_for_input():
    This function asks the user to guess a letter and iteratively checks if it is a single alphabetical character. 

    check_guess(guess): 
    This function checks if the character guessed is in the randomised word. 

During this milestone, the word list used to selected a random word for the game was changed. Previously, this was a short list of 5 words. This was changed to a list of the 1000 most common words, where only words greater than 2 characters was used in the word list. 
