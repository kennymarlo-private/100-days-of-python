from art import logo
from alphabet import alphabet


def caesar(cipher_direction, start_text, shift_amount):
    processed_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char not in alphabet:
            processed_text += char
        else:
            position = alphabet.index(char)
            position += shift_amount
            processed_text += alphabet[position]

    print(f"The {cipher_direction}d text is {processed_text}")


doItAgain = True
print(logo)

while doItAgain:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

    again = input("Do you want to do it again? Type 'yes' or 'no': ")
    if again == "no" or again == "n":
        doItAgain = False
        print("Thank you and see you again!")
