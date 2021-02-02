# Section 04-3
# 파이썬 데이터 타입 (자료형)
# 리스트, 튜플

# 리스트(순서 O, 중복 O, 수정 O, 삭제 O)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']    #다른 data type끼리도 한 list에 넣을 수 있음
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# indexing

print(d[3]) #banana
print(d[-2])    #banana
print(d[0]+d[1])    #int끼리 더한 거니깐 가능가능
print(e[2][1])  #banana
print(e[-1][-2])    #banana

print()

# slicing

print(d[0:2])   #[10, 100]
print(e[2][1:3])    #[Banana, Orange]

print()

# 연산

print(c+d)  #1, 2, 3, 4, 10, 100, pen, banana, orange
print(c*3)  #1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4
print(str(c[0])+'hi')   #1hi

print()

# 리스트 수정, 삭제

c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000] # 중간에 있던 게 뒤로 밀려나고 가운데에 교체&삽입됨
print(c)    #[77, 100, 1000, 10000, 3, 4]
c[1] = ['a', 'b', 'c']
print(c)  #[77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

del c[1]
print(c)    #[77, 1000, 10000, 3, 4]
del c[-1]
print(c)    #[77, 1000, 10000, 3]

print()

#리스트 함수

y = [5, 2, 3, 1, 4]
print(y)
y.append(6) #끝 부분에 삽입
print(y)
y.sort()    #오름차순 정렬
print(y)
y.reverse() #6 5 4 3 2 1
print(y)
y.insert(2, 7)  #(a, b). a번 index에 b를 넣을겨
print(y)
y.remove(2) #2번 index가 아니라 값이 2인 게 지워졌음
print(y)
y.pop() #제일 마지막에 있는 원소 빼기
print(y)    #LIFO
ex = [88, 77]
y.extend(ex)    #y에 ex를 연장시킴. 이건 [원래 리스트, 추가할 원소들]
print(y)
y.append(ex)    #y에 list ex 자체를 삽입하는 거. 그래서 이건 들어갈 때 [원래 리스트, [삽입된 리스트]] 이렇게 들어감. 
print(y)

# 삭제 : del, remove, pop

print()

# 튜플 (순서O, 중복O, 수정X, 삭제X)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])  #c

print(d[2:])    #((a, b, c))
print(d[2][0:2])    #(a, b)

print(c+d)  #(1, 2, 3, 4, 10, 100, ('a', 'b', 'c'))
print(c*3)  #기존 c가 확장. 똑같은 원소 세 번씩~

print()

# tuple 함수

z = (5, 2, 1, 3, 1)
print(z)
print(3 in z)   #True
print(z.index(3))   #3의 값이 있는 곳의 index 반환
print(z.count(1))   #1의 개수가 몇 개인가~ 출력됨  