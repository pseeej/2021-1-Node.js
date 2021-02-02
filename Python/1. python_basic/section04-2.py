# section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am cute."
str2 = "Sejin"
str3=''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4)) #str길이(10 5 0 0)

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)  #"" 출력하는 방법
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)  #Tab    Tab    Tab

print()

# Raw String(있는 그대로 출력하기)
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)   #C:\Programs\Test\Bin
raw_s2 = r"\\a\\a"
print(raw_s2)   #\\a\\a

print()


import sys

# 멀티 라인 #변수 선언하고 \ 나오면 다음 기호가 쭉 이어지는구나 생각하면 됨
multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

print()

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100) # * 백 개
print(str_o2 + str_o3)  #abcdef
print(str_o1 * 3)   #string연산자는 곱셈은 가능하지만 덧셈같은 건 불가
print('a' in str_o4)    #a가 str_o4 안에 있는가? True
print('f' in str_o4)    #f 있냐? False
print('z' not in str_o4)    #z 없지? True

print()

# 문자열 형 변환
print(str(77) + 'a')    # 두 개 다 문자형이라서 덧셈 가능
print(str(10.4))

print()

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'

# print(a.islower())  #다 소문자면 true 아니면 false
# print(a.endswith('s'))  #끝글자가 s로 끝나니?
# print(b.capitalize) #제일 앞 글자만 대문자로
# print(a.replace('nice', 'good'))    #nice의 위치를 good으로 바꾸기
# print(a)    #replace로 변환된 결과
# print(list(reversed(b)))    #list형태로 반환해서 순서 뒤집기

# 문자열은 한 번 할당되면 반환 불가. indexing 때문에

a = 'niceman'
b = 'orange'

print(a[0:3])   #마지막에 있는 수 전까지 나옴. 2까지 나온다~ 출력하면 nic나옴
print(a[0:4])   #nice
print(a[0:len(a)]) #niceman.
print(a[:4])    #nice
print(b[0:4:2]) #0부터 3까지인데 2씩 skip하면서 slicing 처리
print(b[1:-2])  #ran. 끝에서부터 2+1번째 자리까지. ran
print(b[::-1])  #orange를 뒤집어서 출력함. 뒤에서부터 앞으로