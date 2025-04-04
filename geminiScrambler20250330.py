#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 17:43:47 2025

@author: nikodrake-mclaughlin

real author is Gemini




Explanation:
	1	Imports: Import necessary Pygame modules, random for word selection and shuffling, and sys for exiting the game.
	2	Initialization: Initialize Pygame using pygame.init().
	3	Screen Setup: Define screen dimensions and create the display window using pygame.display.set_mode(). Set the window title.
	4	Colors: Define RGB color tuples for easy use.
	5	Fonts: Create Pygame font objects for different text sizes. You can specify font files here if you want custom fonts.
	6	Word List: A list of words that will be used in the game. You can expand this list.
	7	choose_word() Function: Randomly selects a word from the word_list and converts it to uppercase.
	8	scramble_word() Function:
	◦	Takes a word as input.
	◦	Converts the word into a list of characters.
	◦	Uses random.shuffle() to shuffle the letters in place.
	◦	Joins the shuffled letters back into a string.
	9	display_message() Function:
	◦	A helper function to easily display text on the screen.
	◦	Takes the text, color, vertical offset, and size as arguments.
	◦	Renders the text using the specified font.
	◦	Gets the rectangle of the text surface and centers it on the screen (with the offset).
	◦	Blits (draws) the text onto the screen.
	10	display_scrambled_word() Function: Specifically displays the scrambled word at the top of the screen.
	11	display_input_box() Function:
	◦	Draws a rectangle to represent the input box.
	◦	Renders the user's input text within the box.
	◦	Centers the input text within the box.
	◦	Blits the input box and text onto the screen.
	12	game_loop() Function:
	◦	This is the heart of the game.
	◦	Calls choose_word() to get a random word.
	◦	Calls scramble_word() to get the scrambled version.
	◦	Initializes an empty string user_input to store the player's guess.
	◦	Initializes an empty string feedback to display messages to the player.
	◦	Sets the running flag to True to start the game loop.
	◦	Event Handling: The inner loop iterates through Pygame events:
	▪	pygame.QUIT: If the user closes the window, set running to False to exit the loop.
	▪	pygame.KEYDOWN: If a key is pressed:
	▪	pygame.K_BACKSPACE: Removes the last character from user_input.
	▪	pygame.K_RETURN: Checks if the user_input (converted to uppercase) matches the word_to_guess. Updates the feedback message accordingly.
	▪	pygame.K_SPACE: Allows spaces in the input (useful if you have words with spaces).
	▪	event.unicode.isalpha(): Appends the typed letter to user_input.
	◦	Drawing:
	▪	Fills the screen with white to clear the previous frame.
	▪	Calls display_scrambled_word() to show the scrambled word.
	▪	Calls display_input_box() to show the input area and the user's current guess.
	▪	Calls display_message() to show the feedback to the player.
	◦	pygame.display.flip(): Updates the entire screen to show the drawn elements.
	◦	Exiting: Once the loop ends (running is False), quit Pygame and exit the system.
	13	if __name__ == "__main__":: This ensures that the game_loop() function is called only when the script is run directly.
How to Run This Code:
	1	Make sure you have Pygame installed. If not, open your terminal or command prompt and run: Bash

pip install pygame


Save the code: Save the code as a Python file (e.g., word_scramble.py).
Run from the terminal: Navigate to the directory where you saved the file and run:

python word_scramble.py


Possible Next Steps and Improvements:
	•	Difficulty Levels: You could have different word lengths or time limits for different difficulty settings.
	•	Scoring: Keep track of the player's score.
	•	Hints: Implement a hint system (e.g., reveal one letter).
	•	Timer: Add a timer to make the game more challenging.
	•	Visual Enhancements: Add background images, different colors, or more sophisticated UI elements.
	•	Sound Effects: Include sound effects for correct/incorrect guesses.
	•	Multiple Rounds: Allow the player to play multiple rounds.
	•	Word Input: Allow the user to input their own list of words.
	•	Error Handling: Handle cases where the user enters non-alphabetic characters (though the current code tries to address this).
This code provides a solid starting point for your word scramble game. Feel free to modify and expand upon it to create the game you envision!
"""

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Word Scramble")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Fonts
font_large = pygame.font.Font(None, 74)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# Word list (you can expand this)
word_list = ["PYTHON", "GAME", "SCRAMBLE", "CODING", "PYGAME", "DEVELOPER"]

def choose_word():
    """Selects a random word from the word list."""
    return random.choice(word_list).upper()

def scramble_word(word):
    """Scrambles the letters of a word."""
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

def display_message(text, color, y_offset=0, size="medium"):
    """Displays a text message on the screen."""
    if size == "large":
        text_surface = font_large.render(text, True, color)
    elif size == "small":
        text_surface = font_small.render(text, True, color)
    else:
        text_surface = font_medium.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
    screen.blit(text_surface, text_rect)

def display_scrambled_word(scrambled_word):
    """Displays the scrambled word."""
    display_message(scrambled_word, black, -100, "large")

def display_input_box(user_input):
    """Displays the input box for the user's guess."""
    input_box_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 50, 300, 50)
    pygame.draw.rect(screen, black, input_box_rect, 2)
    text_surface = font_medium.render(user_input, True, black)
    text_rect = text_surface.get_rect(center=input_box_rect.center)
    screen.blit(text_surface, text_rect)

def display_input_box2(user_input):
    """Displays the input box for the user's guess."""
    input_box_rect = pygame.Rect(screen_width // 2 - 150, screen_height // 2 + 10, 300, 50)
    pygame.draw.rect(screen, black, input_box_rect, 2)
    text_surface = font_medium.render(user_input, True, black)
    text_rect = text_surface.get_rect(center=input_box_rect.center)
    screen.blit(text_surface, text_rect)

def remove_letter(word, letter):
    """remove the left most copy of specified letter, return word without letter"""
    #issues, how to check properly if word is correct once the _ is there
    #how to integrate delete
    if letter in word:
        word = word.replace(letter, "_", 1)
        
        return word




def game_loop():
    """The main game loop."""
    word_to_guess = choose_word()
    scrambled = scramble_word(word_to_guess)
    user_input = ""
    user_input2 = word_to_guess
    feedback = ""
    running = True

    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    put_back_in_word = user_input[-1].upper()
                    user_input = user_input[:-1]
                    scrambled = scrambled.replace("_", put_back_in_word, 1)
                    
                elif event.key == pygame.K_RETURN:
                    if user_input.upper() == word_to_guess:
                        feedback = "Correct!"
                        word_to_guess = choose_word()
                        scrambled = scramble_word(word_to_guess)
                        user_input = ""
                    else:
                        feedback = "Incorrect. Try again!"
                    user_input = ""
                    scrambled = scramble_word(word_to_guess)
                    
                elif event.key == pygame.K_SPACE:  # Allow spaces if you have words with spaces
                    #user_input += " "
                    scrambled = scramble_word(scrambled)
                    
                elif event.unicode.isalpha(): # Only allow letters
                    if event.unicode.upper() in scrambled:
                        user_input += event.unicode
                        scrambled = scrambled.replace(event.unicode.upper(), "_", 1)
                        user_input2 = scrambled
               
        display_scrambled_word(scrambled)
        display_input_box(user_input)
        display_input_box2(user_input2)
        display_message(feedback, green if feedback == "Correct!" else red, 150)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()