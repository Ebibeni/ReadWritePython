num = int(input('Please enter a number: '))
z = 0

for i in range(2, num // 2 + 1):
    if (num % i) == 0:
        z = z + 1
if z <= 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
