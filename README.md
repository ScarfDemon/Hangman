# Hangman
In this game of hangman, the computer takes a random word from a list of commonly used words. The player then tries to guess the word letter by letter, asking for hints if necessary. The player has a limited number of lives as in a regular hangman game. ==test== 

## Generating a random word
The file [1-1000.txt](https://gist.github.com/deekayen/4148741#file-1-1000-txt) contains a list of commonly used words. This list is then filtered such that the new list only contains words with more than three letters (so that we are not guessing 'a' or 'to' etc.). 

## Hangman Class
A hangman class is created and initialises attributes including the random word (randomised from the passed parameter "word_list") and number of lives (default 5 lives). The word_guessed attribute holds the word needed to be guessed. This starts out initially as underscores the length of the random word, and as guesses are made correctly, underscrores are replaced by the right letters.Other attributes are listed in the code and are labelled with comments.


## Methods of the Hangman Class

### ask_for_input():
This function asks the player to guess a letter and iteratively checks if it is a single alphabetical character, alerting the player if a guess was already made or is invalid.
However if the input contains the word 'hint', the hint method computes. If the input contains the word 'letter' or 'guess', all guessed letters made by the player so far is printed.

### hint():
In the hangman class, a list of unique letters in the word was initialised. With each correct guess, that letter was removed from the list. If the player asks for a hint, a random letter from this list of remaining unique letters is chosen. This letter is then filled out in the word.

### check_guess(guess): 
This function checks if the character guessed is in the randomised word. If the letter is not in the word, the number of lives decreases by one. 
If a letter is guessed correctly, every underscore in the word_guessed attribute (Underscores representing each letter in the word to be guessed) that had the correctly guessed letter was replaced by the letter. 

e.g. if the word was 'cat' and 'a' was guessed, word_guessed would change from ['_', '_', '_']  to ['_', 'a', '_']
    



## play-game function
The play_game function lies outside the Hangman class. In this function, the Hangman class is initialised as 'game'. The play-game function serves to loop until the player has either won or lost. If the number of lives is not zero, and there are no more letters to guess in the num_letters atribute, the player has won!
