list = [1,3,-4,-6,4,8,-3,9]
positive , negative = [], []
for num in list:
    if num>0 :
        positive.append(num)
    else:
        negative.append(num)

print(positive)
print(negative)