num = int(input('Please enter a number: '))
z = 0

for i in range(2, num):
    if (num % i) == 0:
        z = z + i
if z == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")