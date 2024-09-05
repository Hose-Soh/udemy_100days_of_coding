alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    # create an empty list to store the encrypted characters
    string_encrypted = []

    for letter in original_text:
        # ASCII 'a'=97, 'z'=122. If the ASCII value of letter+shift_amount is over 122 then reverse count
        # ord() returns ASCII value of characters, chr() returns character associated to specific digit
        if ord(letter)+shift_amount > 122:
            letter = chr(ord(letter) - (26-shift_amount))
            string_encrypted.append(letter)
        # if letter+shift_amount is less than 122, increase the ASCII value
        else:
            letter = chr(ord(letter) + shift_amount)
            string_encrypted.append(letter)
    # convert list to string and print
    print("".join(string_encrypted))


encrypt(text, shift)