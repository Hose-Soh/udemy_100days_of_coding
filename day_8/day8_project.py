# import art.py file
import art

# print logo from art.py
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        # encode or decode only the characters from a-z otherwise keep them as it is
        if 97<=ord(letter)<=122:
            if encode_or_decode == "decode":
                shift_amount *= -1
            elif encode_or_decode == "encode":
                shift_amount *= 1
            else:
                print("Wrong Input")

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text+=letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# run indefinite while loop
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    run_again = input("Do you want to continue? y/n: ")
    if run_again=='y':
        continue
    else:
        break


