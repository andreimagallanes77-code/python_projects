input_text = input("Enter a string: ")
uppercase_text = ""

for character in input_text:
    if 'a' <= character <= 'z':
        uppercase_text += chr(ord(character) - 32)
    else:
        uppercase_text += character

print("Uppercase:", uppercase_text)
