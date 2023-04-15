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
def Key(message, keyword):
    keyword = list(keyword)
    if len(message) == len(keyword):
        return(keyword)
    else:
        for i in range(len(message) - len(keyword)):
            keyword.append(keyword[i])
    return("" . join(keyword))

# encrypt text
def cipherNum(message, key):
    cipher_text = []
    for i in range(len(message)):
        add_mod = (ord(message[i]) + ord(key[i])) % 26
        add_mod += 0
        cipher_text.append(str(add_mod))
    return(" " . join(cipher_text))

def cipherText(message, key):
    cipher_text = []
    for i in range(len(message)):
        add_mod = (ord(message[i]) + ord(key[i])) % 26
        add_mod += ord('A')
        cipher_text.append(chr(add_mod))
    return(" " . join(cipher_text))
     
message = message_input
keyword = key_input
key = Key(message, keyword)
cipher_text = cipherText(message,key)
num = cipherNum(message, key)

# print ciphertext
print("Loading Loading Loading.... \n")
console.print("✔ Untranslated numbers :", num + "\n", style = "num_num")
console.print(":heart: The ciphertext :", cipher_text + ":heart: \n", style = "cipher")

