print("Enter numbers (type a non-number to stop)")

numbers = []

while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        break
    numbers.append(int(user_input))

if numbers:
    most_common = numbers[0]
    for num in numbers:
        if numbers.count(num) > numbers.count(most_common):
            most_common = num
    print("Number with the most duplicates is:", most_common)
else:
    print("No valid numbers were entered.")