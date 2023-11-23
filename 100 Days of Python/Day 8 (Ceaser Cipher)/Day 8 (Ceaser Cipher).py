alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(direction, text, shift):
    cipher_text = ""
    if direction == "decode":
            shift *= -1
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index + shift
            new_letter = alphabet[new_index]
            cipher_text += new_letter
        else:
             cipher_text += char   
    print(f"The {direction}d text is {cipher_text}")



question = True
while question :   
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26 
        caeser(direction, text, shift)
        result = input("yes or no")
        if result == 'no':
            question = False
            print('Goodbye')





