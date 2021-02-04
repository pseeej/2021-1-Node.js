# section 07-1
# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명 :
#     함수
#     함수
#     함수


# 예제 1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name): # 클래스 최초 초기화
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)
    

# 네임스페이스 : instance가 갖고 있는 각각의 저장 공간
user1 = UserInfo("Sejin")   #인스턴스화. 할당하는 거
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))    #이거 값 두 개 다 다름. user1과 user2는 다른 것임을 확인 가능
print(user1.__dict__)
print(user2.__dict__)


print()

# 예제 2
# self의 이해
class SelfTest :
    def function1():    # 클래스 method. 여러 instance들이 공용으로 사용하는 함수. 호출할 때는 class로 해서 호출해야됨
        print('function1 called')
    def function2(self):    # instance 함수
        print(id(self)) # self로 하면 이거 값 다 같음
        print('function2 called!')

self_test = SelfTest()
#self_test.function1()  이거 호출 안 됨. function1이 self를 갖고 있지 않아서 instance화 안 됨을 확인할 수 있음. 
SelfTest.function1()    # function1 쓰려면 이렇게 class로 해서 써야됨
self_test.function2()   # 이건 가능

print(id(self_test))
SelfTest.function2(self_test)   #이렇게 class로 불러놓고 self 안에 넣어주는 방식은 가능

# 예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse :
    # 클래스 변수 (self 없음)
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num +=1 #생성될 때마다 이거 호출됨
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)   # 클래스 네임스페이스, 클래스 변수 (공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)  # 자기 namespace에 없으면 class의 namespace 가서 찾아냄. 그래서 이렇게 해도 stock_num의 값 출력되는겨
print(user2.stock_num)
print(user3.stock_num)

del user1   # instance 지움. class 내에 있는 __del__ 호출됨 => stock_num -= 1 실행됨
print(user2.stock_num)
print(user3.stock_num)