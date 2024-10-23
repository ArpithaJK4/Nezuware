# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:10:48 2024

@author: admin
"""

import random

# List of possible words
word_list = ['python', 'hangman', 'development', 'computer', 'algorithm', 'datascience', 'programming']

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to display the hangman stages
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,  # Final state: Head, torso, both arms, and both legs
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,  # Head, torso, both arms, and one leg
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,  # Head, torso, and both arms
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,  # Head, torso, and one arm
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,  # Head and torso
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,  # Head
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """  # Empty state
    ]
    return stages[tries]

# Function to play one round of the game
def play_round():
    word = random.choice(word_list).lower()
    guessed_letters = []
    tries = 6
    word_guessed = False
    
    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(display_word(word, guessed_letters))
    
    while tries > 0 and not word_guessed:
        guess = input("\nGuess a letter: ").lower()

        # Input validation: Ensure the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please guess a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try again.")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"Sorry! '{guess}' is not in the word. You have {tries} attempts left.")
        
        # Display the current state of the word and the hangman
        print(display_hangman(tries))
        print(display_word(word, guessed_letters))

        # Check if the word has been fully guessed
        if all([letter in guessed_letters for letter in word]):
            word_guessed = True

    # End of the game
    if word_guessed:
        print(f"Congratulations! You guessed the word '{word}'.")
    else:
        print(f"Game Over! The word was '{word}'.")

# Function to manage multiple games
def hangman_game():
    while True:
        play_round()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
hangman_game()
