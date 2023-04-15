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