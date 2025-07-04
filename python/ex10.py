a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))
c = int(input("세 법째 정수: "))

if a > b:
    if b > c:
        print(c)
    else:
        print(b)
else:
    if a > c:
        print(c)
    else:
        print(a)