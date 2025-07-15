import random

def guess_number():
    answer = random.randint(1,100)
    tries = 0

    print("1부터 100 사이의 숫자를 맞춰보세요")
    while True:
        guess = int(input("숫자를 입력하세요: "))
        tries += 1
        if guess < answer:
            print("더 큰 숫자입니다.")
        elif guess > answer:
            print("더 작은 숫자입니다.")
        else:
            print(f"정답입니다! 시도 횟수: {tries}")
            break
if __name__ == "__main__":
    guess_number()