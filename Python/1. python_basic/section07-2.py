# section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중 상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모 

class Car :     # 부모 클래스
    """Parent Class"""
    def __init__(self, tp, color):
        self.type =tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BMWCar(Car):  # 자식 클래스
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 겹치는 부분 부모에게 넘겨줌.
        self.car_name = car_name
    
    def show_model(self) -> None:   #None은 그냥 hint를 준 거. 정답이 없다~
        return "Your Car Name : %s" %self.car_name

class BenzCar(Car): 
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) 
        self.car_name = car_name
    
    def show_model(self) -> None:   
        return "Your Car Name : %s" %self.car_name

    def show(self):
        print(super().show()) # 부모에 있는 show method 호출
        return 'Car Info : %s %s %s' %(self.car_name, self.type, self.color)

# 일반 사용 방법
model1 = BMWCar('520d', 'sedan', 'red') # 인스턴스 생성

# 자식한테 없는 건 부모에서 알아서 가져옴. 부모, 자식에 있는 내용들 자유롭게 왔다갔다 이용 가능
print(model1.color) # 부모에서 가져옴
print(model1.type)  # 부모에서 가져옴
print(model1.car_name)  # 자식에서 가져옴
print(model1.show())    # 부모에서 가져옴
print(model1.show_model())  # 자식
print(model1.__dict__)

print()

# Method overriding(오버라이딩). code 재활용 가능
model2 = BenzCar("220d", 'suv', "black")
print(model2.show())    #부모한테 있는 method가 자식한테도 같은 이름으로 있으면 자식 거 사용함

print()

# Parent Method Call
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())    #overriding된 show호출됨

print()

# Inheritance Info (상속 정보)
print(BMWCar.mro()) #상속 관계 나타남. BMW <- Car <- Object(모든 class의 부모는 object이기 때문)
print(BenzCar.mro())

print()

# 예제 2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())  #[<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
print(A.mro())  #[<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]
