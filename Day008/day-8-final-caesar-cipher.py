from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_len = len(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
            shift_amount *= -1
    
    for char in start_text:
        if char in alphabet:    
            position = alphabet.index(char)

            if cipher_direction == "encode":
                position = position - alphabet_len
            
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += char
    
    print(f"The {cipher_direction}d text is '{end_text}'")

print(logo)

should_continue = True

while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    continues = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if continues == "no":
        should_continue = False
        print("Good Bye!")
