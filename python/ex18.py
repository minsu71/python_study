import random

x = input("가위,바위,보 중에 선택하세요: ")
num1 = random.randint(0, 2)

if x == "가위":
    s = 0
elif x == "바위":
    s = 1
elif x == "보":
    s = 2
else:
    print("가위,바위,보 중에서 입력하세요.")

print(num1, x)


if num1 == s:
    print("비겼습니다.")
elif num1 == 0:
    if s == 1:
        print("이겼습니다.")
    else:
        print("졌습니다.")
elif num1 == 1:
    if s == 0:
        print("졌습니다.")
    else:
        print("이겼습니다.")
elif num1 == 2:
    if s == 0:
        print("이겼습니다.")
    else:
        print("졌습니다.")