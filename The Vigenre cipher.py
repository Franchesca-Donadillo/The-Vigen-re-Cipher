# Franchesca Marie Donadillo
# BSCPE 1-5
# ASSIGNMENT 2_Problem 3 - The Vigenère Cipher

# importing for design
from rich.console import Console
from rich.theme import Theme

theme_personalize = Theme({"theTitle" : "bold violet", "input" : "italic blue", "cipher" : "blink bold green", "num_num" : "yellow"})
console = Console(theme = theme_personalize)

# activity title
title = "The Vigenère Cipher\n"
new_title = title.center(55).upper()
console.print(new_title, style = "theTitle")

# ask user for input message and key
message_input = input("Enter your message: ").upper()
key_input = input("Enter your key: ").upper()

# print uppercase letters of the user input
console.print("="*60, "\n\n" + message_input.center(55), style = "input")
console.print(key_input.center(55), "\n\n" + "="*60, style = "input")

# generating the key 
# encrypt text
# print ciphertext