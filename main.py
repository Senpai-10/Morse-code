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
    '(':'-.--.', ')':'-.--.-', '!': '-.-.--',
    '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    '¿': '..-.-', '¡': '--...-'
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
    msg += ' '
  
    decipher = '' 
    citext = '' 
    for letter in msg: 
  
        if (letter != ' '): 
  
            i = 0
            citext += letter 

        else: 
            i += 1
  
            if i == 2 : 
  
                decipher += ' '
            else: 
  
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = ''
  
    return decipher 

def main():
    print('1. encrypt')
    print('2. decrypt')
    option = input("$ ")
    
    if option == '1' or option == 'encrypt':
        text = input("text $ ")
        print(encrypt(text))

    if option == '2' or option == 'decrypt':
        code = input("morse code $ ")
        print(decrypt(code))


if __name__ == "__main__":
    main()
    os.system("pause")