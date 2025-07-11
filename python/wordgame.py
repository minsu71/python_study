import random
import time

words = ["사과", "오렌지", "바나나", "포도", "수박", "참외", "귤", "코코넛", "딸기"]

health = 3
score = 0


while True:
    word = random.choice(words)
    start = time.time()
    print(word)
    x = input("단어를 입력하세요: ")
    end = time.time()
    times = end -start
    print("시간:", times)
    if word == x and times < 2:
        print("정답입니다.")
        score = score + 1
        print("현재 점수: ", score)
    elif word != x or times > 2:
        health = health - 1
        print("현재 남은 목슴:", health)
        if health == 0:
            print("목슴이 끝났습니다.")
            break