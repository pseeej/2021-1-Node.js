# section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명 (parameter):
#   code

# 함수 호출
# 함수 설명 (parmaeter)

# 함수 선언 위치 중요

# 예제 1
def hello(world):
    print("Hello, ", world)
hello("Python!")
hello(7777)

print()

# 예제 2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!!!")
print(str)

print()

# 예제 3(다중 리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x*200
    y3 = x*300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1,  val2, val3)

print()

# 예제 4(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x*200
    y3 = x*300
    return [y1, y2, y3] #원래 각각은 다 int형이었는데 return []로 list형 반환 가능

lt = func_mul2(100)
print(lt, type(lt))

print()

# 예제 5
# *args, *kwargs

def args_func(*args):   #여러 개를 인자로 받아도 각각 다 처리 가능
    print(args) #tuple 형태로 출력됨
    
    for i, v in enumerate(args):    #i로 index 만들어서 순회 가능. 
        print(i, v)

args_func('Park')
args_func('park', 'kim')
args_func('kim', 'park', 'lee')

print()

# *kwargs(keyword args)

def kwargs_func(**kwargs):  #dict 형태가 인자로 넘어감
    for k, v in kwargs.items():
        print(k, v) #key, values

kwargs_func(name1='Kim', name2='Park', name3='Lee')
kwargs_func(nme1='Kim')

print()

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20) #10 20 () {}
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)    #10 20 ('park', 'kim') {'age1': 24, 'age2': 35}

print()

# 예제 6
# 중첩 함수(클로저)
def nested_func(num):
    def func_in_func(num):  #이 부분은 그냥 함수 정의
        print('>>>',num)
    print("in func")
    func_in_func(num+10000) #이게 함수 사용

nested_func(10000)

print()

# 예제 7(hint)
def func_mul3(x : int) -> list: #꼭 int형으로 받아서 list형으로 return해야해
    y1 = x * 100
    y2 = x*200
    y3 = x*300
    return [y1, y2, y3]

print(func_mul3(5))

print()

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num:int) -> int:
    return num*10

var_func = mul_10   #변수에 할당해둠. 함수 사용 안 해도 메모리에 이미 함수 올라가있음 확인 가능
print(var_func)
print(type(var_func))   #function type

print(var_func(10))

lambda_mul_10 = lambda x : x*10 #위의 fucntion mul_10과 같은 내용

print(">>>", lambda_mul_10(10))

def func_final(x, y, func): #매개변수로 함수 받을 수 있음~
    print(x*y*func(10))

func_final(10, 10, lambda_mul_10)   #10000

print(func_final(10, 10, lambda x:x*1000))  #100000. None 뜨는 건 그냥 출력할 게 없어서 뜬겨