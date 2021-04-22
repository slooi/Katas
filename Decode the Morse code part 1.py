MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

def decodeMorse(morse_code):
    """
    NOTES:
        - 3 spaces = word seperation 
        - 1 space = letter character
        - EXTRA spaces efore and after should be ignored
        - special codes are treated as single special characters, and usually are transmitted as separate words
        - 
    IMPLEMENT:
        - keep recording until there's a space
        - when there's a space save word.
            - Remember 1 space = letter, 3 space = word
    """
    # Remove trailing whitespace and separate different words into different elements
    word_arr = morse_code.strip().split("   ")
    # Separate each letter into its own element
    word_arr = [word.split(" ") for word in word_arr]

    sentence = ""
    for i, word in enumerate(word_arr):
        for letter_code in word:
            sentence+=MORSE_CODE[letter_code]
    
        # Add " " after word unless it's the last word
        if not i == len(word_arr)-1:
            sentence+=" "
    
    return sentence

# print(flatten([1,2,3,[1,[2]]]))
# print(flatten([[3,3,3,3,3],1,2,3,[1,2]]))
print(decodeMorse('     .... . -.--   .--- ..- -.. .          '))
