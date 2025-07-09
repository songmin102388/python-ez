import random

def number():

    print("컴퓨터가 선택한 숫자를 사용자가 맞추는 게임입니다.")
   
    a = random.randint(1, 100)
    s = 0
    rember =[]

    print("1부터 100 사이의 숫자를 맞춰보시오.")

    while True:
        try:
            f = int(input("숫자를 입력하세요: "))
            s += 1
            rember.append(f)

            if f < a:
                print("up")
            elif f > a:
                print("down")
            else:
                print(f"정답입니다! {s}번 만에 맞추셨습니다.")
                print("입력한 숫자 목록:", rember)
                break
                
        except ValueError:
            print("유효한 숫자를 입력하시오.")

if __name__ == "__main__": 
    number()

    