alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    alphabet_len = len(alphabet)

    for letter in start_text:
        position = alphabet.index(letter)

        if cipher_direction == "encode":
            position = position - alphabet_len
            new_position = position + shift_amount
        elif cipher_direction == "decode":
            new_position = position - shift_amount
        
        new_letter = alphabet[new_position]
        end_text += new_letter

    print(f"The {cipher_direction}d text is {end_text}")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
