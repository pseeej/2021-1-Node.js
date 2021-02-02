# 가상환경 설치한 거에서 들어오기
# 실행은,,, ctrl+alt+n

# dataType 종류 : boolean, numbers, string, bytes, lists, typles, sets, dictionaries(, complex)
# 연산자 : +, -, *, /, //(나눗셈 한 몫), %, **(제곱), 단항 연산자

v_str1 = "Niceman"
v_bool = True
v_float = 10.3
v_int = 7
v_dict = {  # key : value
    "name" : "Park",
    "age" : 23,
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))

print()

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777
f1 = 1.2345
f2 = 3.784
f3 = .5 # 0.5
f4 = 10.    # 10.0

print(i1*i2)
print(big_int1*big_int2)
print(f1**f2)
print(f3 + i2)  #자동으로 형변환 일어나서 계산됨 (int->float)

print()

# 자동 형변환
# int, float, complex (복소수)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a+b
print(result2)

print()

# 강제 형변환

print(int(result2)) #9
print(float(c)) #10.0
print(complex(3))   #3+0j
print(int(True))    #1
print(int('3')) #3
print(complex(False))   #0j

print()

# 단항 연산자

y=100
y += 100 #y=y+100
print(y)

print()

# 수치 연산 함수
# http://docs.python.org/3/library/math.html

print(abs(-7))  #절대값 씌워줌. 7
n, m = divmod(100, 8)   #몫은 n 나머지는 m에 들어감
print(n, m) #12 4

import math
print(math.ceil(5.1))   #숫자 올림함
print(math.floor(3.82541))  #숫자 내림함

