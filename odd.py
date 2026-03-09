odd_count = 0

for count in range(10):
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        odd_count = odd_count + 1

print("Total odd numbers:", odd_count)