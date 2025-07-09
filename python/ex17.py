import random

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
x = random.randint(0,3)


if x ==0:
    sum = int(num1+num2)
elif x==1:
    sum = int(num1-num2)
elif x==2:
    sum = int(num1*num2)
else:
    sum = int(num1/num2)

print(num1, num2)
print(x)
print(sum)