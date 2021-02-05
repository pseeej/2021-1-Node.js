# section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크


# SyntaxError : 잘못된 문법

# print('Test)
# if True 
#   pass
# x>=y


# NameError : 참조변수 없음

a = 10
b = 15
#print(c)


# ZeroDivisionError : 0 나누기 에러
# print(10/0)


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3])   # 예외 발생


# KeyError

dic = {'name' : 'Park',  'age' : 23, 'City' : 'Seoul'}
# print(dic['hobby'])
print(dic.get('hobby')) #위에랑 동일한데 이렇게 작성해주면 오류 없이 그냥 없다는 None이 출력됨


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month()) 없는 모듈 사용하려고 함


# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 6]

# x.remove(10)
# x.index(10)


# FileNotFoundError. 주로 외부 파일 처리할 때 발생하는 에러

# f = open('test.txt', 'r'). 예외 발생


# TypeError

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x+y)  #typeError. list와 tuple 서로 계산 불가
print(x+list(y))    # 이렇게 작성하는 건 가능


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외 처리 코딩 권장 (EAFP 코딩 스타일)

print()

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1

name = ['Kim', 'Lee', "Park"]
try : 
    z = 'Kim'   # cho 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError : #error명
    print('Not found it! - Occurred ValueError!')   # error 발생 시 실행할 코드
else :
    print('Ok! else!')  # error 발생 없이 정상 작동될 때만 실행됨


print()

# 예제 2
try : 
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except  :   # 어떤 error가 발생할ㅈㅣ 모를 땐 그냥 비워둠. 이렇게 되어있을 땐 어떤 에러가 발생하든 다 이 구문 거쳐가게 되는겨
    print('Not found it! - Occurred Error!')
else :
    print('Ok! else!')

print()

# 예제 3
try : 
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except  :
    print('Not found it! - Occurred Error!')
else :
    print('Ok! else!')  # 에러 발생하지 않았을 때만 실행됨
finally :
    print('Finally ok!')    # 에러가 발생하든 발생하지 않든,,, 무조건적으로 실행되는 코드

print()

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try :
    print('Try')
finally:
    print('OK Finally!')    # 최후에 마지막으로 실행하고 빠져나가는 코딩 패턴

print()

# 예제 5
try : 
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))

except ValueError as l:
    print(l)    # 하면 error가 발생하는 내용이 알아서 출력될 수 있음
    print('Not found it! - Occurred ValueError!')
except IndexError:
    print('Not found it! - Occurred IndexError!')
except Exception:   # 이건 모든 error에 대해 실행됨. 이것도 저것도 아닐 때 이거 수행되도록.
    print('Not found it! - Occurred Error!')
else :
    print('Ok! else!') 
finally :
    print('Finally ok!')

print()

# 예제 6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try :
    a = '333'
    if a == 'Lim' :
        print('허가!')
    else:
        raise ValueError    #원래의 valueError은 이런 내용은 아니지만 프로그래머가 임의로 이렇게 직접 규정할 수 있음
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print("OK")