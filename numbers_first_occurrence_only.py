numbers = []

for i in range(10):
    numbers.append(int(input("Enter a number: ")))

displayed = []

for n in numbers:
    if n not in displayed:
        print(n)
        displayed.append(n)