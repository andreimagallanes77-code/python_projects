numbers = []

for i in range(5):
    numbers.append(int(input("Enter a number: ")))

for n in numbers:
    if numbers.count(n) == 1:
        print(n)
else:
        print("no unique numbers!!!")