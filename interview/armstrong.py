n = int(input("enter a number"))
l = (len(str(n)))
ams = 0

while(n != 0):
    digit = n % 10
    ams = (ams)+ digit ** l
    n //= 10

print(ams)