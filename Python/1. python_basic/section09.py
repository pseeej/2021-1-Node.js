# section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로

# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close resource 반환
f.close()

print()
print()

# 예제 2
with open('./resource/review.txt', 'r') as f:   #위에 거 open문이랑 동일함. 대신에 이거는 따로 내가 close 안 해도 됨
    c = f.read()
    print(c)
    print(list(c))  # list단위로 가져옴
    print(iter(c))  # iterator 반환. for문에서 사용 가능

print()
print()

# 예제 3
with open('./resource/review.txt', 'r') as f:
    for c in f: # c 자체가 iterator로써 사용 가능. 
        print(c.strip())    # 양쪽 공백 지워주고 전체 내용 출력함

print()
print()

# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 위의 문서 다 읽고 마지막에 내가 여기 읽었어~ 하는 커서가 문서의 제일 끝에 위치하므로 
    print(">", content) # 이거 해도 content가 출력되지는 않음. 내용 없음

print()
print()

# 예제 5
with open('./resource/review.txt', 'r') as f:
    line = f.readline() # 줄별로 읽어오기
    # print(line)
    while line: #while문으로 전체 도는 중
        print(line, end='### ')
        line = f.readline()

print()
print()

# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents) # 모든 문장을 enter를 기준으로 list 형태
    for c in contents:
        print(c, end = ' **** ')

print()
print()

# 예제 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line)) #text파일에 있는 건 다 string형태로 반환되므로 int()로 형변환
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

print()
print()



# 파일 쓰기
# 예제 1    (신규 파일에 글 작성하기)
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman\n')

# 예제 2    (기존에 존재하던 파일에 내용 추가하기)
with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')

# 예제 3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))    # 0부터 50 사이의 랜덤한 숫자를 f에 작성ㅎㅐ라~
        f.write('\n')   # 개행문자

# 예제 4 (list로 된 걸 작성하기)
# writelines : 리스트를 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제 5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contents!1', file=f)
    print('Test Contents2!', file=f)    # console에 찍히는 게 아니라 마지막에 file=f로 함으로써 text4.txt 에 입력되는 형태임.