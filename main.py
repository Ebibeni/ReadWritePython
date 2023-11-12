
# count number 1 to 100 and look for a multiple of 3 , 5. thats what 5 & 3 can divide to get 0

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print(x, " is a multiple of both 3 and 5")
    elif x % 3 == 0:
        print(x, " is a multiple of 3")
    elif x % 5 == 0:
        print(x, " is a multiple of 5")
    else:
        print(x)