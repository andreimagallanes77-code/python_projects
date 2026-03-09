lowest = None

while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        break

    number = int(user_input)

    if lowest is None or number < lowest:
        lowest = number

print("The lowest number entered is:", lowest)