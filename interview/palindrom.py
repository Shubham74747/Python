n = int(input("enter a number"))
l = (len(str(n)))
p = 0
if (l%2 != 0):
    while(l > 2):
        digit = n%10
        p = (p*10) + digit
        n //= 10

if (p == n):
    print("The number is palindrom")
else:
    print("Given number is not pelindrom")


# a = input("Enter a string: ")
# b = (a[::-1])
# if(a == b):
#     print("String is pelindrom")
# else:
#     print("String is not pelindrom"