# section 05-2
# python 흐름제어 (반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1<11:
    print("v1 is :", v1)
    v1 += 1

print()

for v2 in range(10):    #0부터 9까지
    print("v2 is :", v2)

print()

for v3 in range(1, 11): #1부터 10까지
    print("v3 is :", v3)

print()

# 1~100 합

sum1 = 0
cnt1 = 1

while cnt1<=100:
    sum1+=cnt1
    cnt1 += 1

print('1~100 : ', sum1)
print('1~100 : ', sum(range(1, 101)))   #위랑 동일
print('1~100 : ', sum(range(1, 101, 2)))    #1부터 100까지의 값을 2 단위로 건너뛰면서 더함

print()

# sequence(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable : range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for name in names:
    print("You are : ", name)

print()

word = "dreams"

for s in word:
    print("Word : ", s) #한 글자씩 출력됨

print()

my_info = {
    "name" : "Kim",
    "age":23,
    "city":"Seoul"
}

# 기본 값은 key
for key in my_info :    
    print("my_info", key)

print()

# 값
for value in my_info.values():
    print("my_info value", value)

print()

# key
for key in my_info.keys():
    print("my_info key", key)

print()

# key and value
for k, v in my_info.items():
    print("my_info key / value", k, v)

print()

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

print()

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 28]

for num in numbers:
    if num==33:
        print("found : 33")
        break
    else:
        print("not found 33")

print()

# for - else 구문 (반복문이 정상적으로 수행된 경우 else 블럭 수행)
for num in numbers:
    if num==54:
        print("found : 33")
        break
    else:
        print("not found 33")
else:   #break문으로 빠져나오면 이거 안 거침
    print("not found 33................")

print()

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue    #아래 부분 수행 없이 바로 다시 조건문으로 들어감
    print("타입 : ", type(v))