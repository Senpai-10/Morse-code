import os

MORSE_CODE_DICT = { 
    'A':'.-', 'B':'-...', 
    'C':'-.-.', 'D':'-..', 'E':'.', 
    'F':'..-.', 'G':'--.', 'H':'....', 
    'I':'..', 'J':'.---', 'K':'-.-', 
    'L':'.-..', 'M':'--', 'N':'-.', 
    'O':'---', 'P':'.--.', 'Q':'--.-', 
    'R':'.-.', 'S':'...', 'T':'-', 
    'U':'..-', 'V':'...-', 'W':'.--', 
    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
    '1':'.----', '2':'..---', '3':'...--', 
    '4':'....-', '5':'.....', '6':'-....', 
    '7':'--...', '8':'---..', '9':'----.', 
    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
    '?':'..--..', '/':'-..-.', '-':'-....-', 
    '(':'-.--.', ')':'-.--.-'
} 

# encrypt the string according to the morse code chart 
def encrypt(msg):
    cipher = '' 
    for letter in msg.upper(): 
        if letter != ' ': 
            
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            cipher += ' '
    return cipher 

# decrypt the string from morse to english 
def decrypt(msg):
    ...

