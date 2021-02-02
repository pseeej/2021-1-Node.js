# Section 04-4
# 파이썬 데이터 타입 (자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(dictionary) : 순서 X, 중복 X, 수정 O, 삭제 O. 어떤 자료형이든 다 넣을 수 있음

# Key, value (Json) -> MongoDB

# 선언
a = {'name' : 'Kim', 'Phone' : '010-7777-7777', 'birth':870214}  #key는 중복 안 되지만 value는 가능
b = {0 : 'Hello Python', 1:'Hello Coding'}
c = {'arr':[1, 2, 3, 4, 5]}

# 출력
print(a['name'])    #name이라는 key의 value값 출력됨
print(a.get('name'))    #위에 것보단 이게 더 안전함
print(a.get('address')) #none
print(c['arr'][1:3])    #list slicing 처리 되기 때문에 이것도 가능

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2, 3,)
print(a)

print()

# keys, values, items
# item은 key:value의 한 쌍
print(a.keys()) #dict_keys(['name', 'Phone', 'birth', 'address', 'rank', 'rank2'])
print(list(a.keys()))   #['name', 'Phone', 'birth', 'address', 'rank', 'rank2']

temp = list(a.keys())
print(temp[1:3])    #['Phone', 'birth']. slicing해서 쓰려면 형 변환해서 써야됨. 기본이 dictionary형태거든~

print(a.values())   #dict_values(['Kim', '010-7777-7777', 870214, 'Seoul', [1, 3, 4], (1, 2, 3)])
print(list(a.values())) #['Kim', '010-7777-7777', 870214, 'Seoul', [1, 3, 4], (1, 2, 3)]. list로 형변환

print(a.items())    #dict_items([('name', 'Kim'), ('Phone', '010-7777-7777'), ('birth', 870214), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))])
print(list(a.items()))

print(2 in b) #key가 2인 게 b에 있냐
print('name' in a)  #'name'이 key에 있냐?

print()

# 집합(sets) (순서 X, 중복 X)
a = set()
b = set([1, 2, 3,4])
c = set([1, 4, 5, 6, 6])

print(type(a))  #set
print(c)    #1, 4, 5, 6

# 집합에서 형 변환해서 원하는 기능 사용 가능

t = tuple(b)
print(t)
l = list(b)
print(l)

print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))  #교집합
print(s1&s2)    #교집합

print(s1|s2)    #합집합
print(s1.union(s2)) 

print(s1-s2)    #차집합
print(s1.difference(s2))

print()

# 추가 & 제거

s3 = set([7, 8, 10, 15])
s3.add(18)  #추가
print(s3)

s3.remove(15)   #15의 값을 지우겠다
print(s3)
