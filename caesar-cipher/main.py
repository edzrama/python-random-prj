from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)
repeat = "yes"


def encrypt(word, shift_number):
    cipher_text = ""
    if shift_number > 26:
        shift_number = shift_number % 26
    for char in word:
        is_letter = False
        for index, letter in enumerate(alphabet):
            if char == letter:
                is_letter = True
                if (index + shift_number) > (len(alphabet) - 1):
                    cipher_text += alphabet[(index + shift_number) - len(alphabet)]
                else:
                    cipher_text += alphabet[index + shift_number]
        if not is_letter:
            cipher_text += char
    print(f"the encoded text is {cipher_text}")


def decrypt(word, shift_number):
    decipher_text = ""
    for char in word:
        is_letter = False
        for index, letter in enumerate(alphabet):
            if char == letter:
                is_letter = True
                decipher_text += alphabet[index - shift_number]
        if not is_letter:
            decipher_text += char
    print(f"the decoded text is {decipher_text}")


while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in ["encode", "decode"]:
        print("Wrong input")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift %= 26
        if direction == "encode":
            encrypt(text, shift)
        else:
            decrypt(text, shift)
    repeat = input('Type "yes" if you want to go again. Otherwise type "no".').lower()
print("Goodbye!")
