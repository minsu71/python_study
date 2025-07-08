a = int(input("키를 입력하세요: "))
b = (a - 100)*0.9

if b >= 50:
    print("과체중")
elif b == 50:
    print("표준체중")
else:
    print("저체중")