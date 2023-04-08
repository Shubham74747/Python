# Python Program to sort characters of string in ascending order.
# str = input("enter  a string : ")
# a =  sorted(str)
# print(a)


# Python Program to sort character of string in descending order.
# str = input("enter  a string : ")
# a = ','.join(sorted(str , reverse=True))
# print(a)


# Python program to copy one string to another string.
# str1 = ("Hello Shubham")
# str2 = ""
# for i in str1:
#     str2 = str2 + i

# print(str2)



# Python program to print all non repeating character in string
str1 = input("enter a string")
result = ''
for i in str1:
    count = 0
    for j in range:
        if i==j:
            count = count+1
            if count > 1:
                break
            if count == 1:
                result += i

print("non repeating element :",result)