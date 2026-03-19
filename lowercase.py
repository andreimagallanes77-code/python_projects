
input_text = input("Enter a string: ")
lowercase_text = ""

for character in input_text:
    if 'A' <= character <= 'Z':
        lowercase_text += chr(ord(character) + 32)
    else:
        lowercase_text += character

print("Lowercase:", lowercase_text)