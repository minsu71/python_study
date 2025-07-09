import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
x = random.randint(0,3)


if x ==0:
    sum = num1+num2
    reply = int(input("{0}+{1}의 값은?" .format(num1, num2)))
    if reply == sum:
        print("정답입니다.")
    else:
        print("틀렸습니다.")
elif x==1:
    sum = num1-num2
    reply = int(input("{0}-{1}의 값은?" .format(num1, num2)))
    if reply == sum:
        print("정답입니다.")
    else:
        print("틀렸습니다.")

elif x==2:
    sum = num1*num2
    reply = int(input("{0}*{1}의 값은?" .format(num1, num2)))
    if reply == sum:
        print("정답입니다.")
    else:
        print("틀렸습니다.")

else:
    sum = num1/num2
    reply = int(input("{0}/{1}의 값은?" .format(num1, num2)))
    if reply == sum:
        print("정답입니다.")
    else:
        print("틀렸습니다.")