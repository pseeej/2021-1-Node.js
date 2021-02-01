# python 기초 코딩
# 몸풀기 코딩 실습

# import this # 걍 파이썬 만든 사람의 주저리문
import sys

# 파이썬 기본 인코딩이 UTF-8이다~ 알 수 있음
print(sys.stdin.encoding)   # utf-8
print(sys.stdout.encoding)  # utf-8

print()

# 출력문
print('My name is Sejin!')

print()

# 변수 선언. 값 선언해서 할당하는 것
myName = 'Sejin'

# 조건문
if myName == 'Sejin' :
    print("OK")

print()

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = '%(i, j), i*j) #구구단 출력

print()

# 변수 선언 (한글)
이름 = "좋은 사람"
print(이름) # 한글로 변수 선언이 되기도 해~

print()

# 함수 선언 (한글, 영문 두 개 다 가능)
def 인사():
    print("안녕하세요, 반갑습니다")

인사()

def greeting():
    print("Hello")

greeting()

print()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))