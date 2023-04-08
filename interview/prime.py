# n = int(input("enter a number : "))
# prime = True

# for i in range(2,n+1):
#     if (n%i == 0):
#         prime = False
#         break

# if prime:
#     print("Given number is prime")
# else:
#     print("Given number is not prime")


#compare btw 2 number prime or not


num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

for num in range(num1, num2+1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)




