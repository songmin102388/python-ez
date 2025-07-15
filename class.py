class person:
    def __init__(self, name, age):
        self.name =name
        self.age =age

    def greet(self):
        print(f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다.")

# 사용 예시
person1 = person("송민", 17)
person1.greet()