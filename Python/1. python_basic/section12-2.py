# section 12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# db 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Users/jinny/OneDrive/바탕 화면/20180368/2021-겨울/FastCampus/BackEnd/Python/1. python_basic/resource/database.db')   # 내 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute('SELECT * FROM users')

# 커서 위치가 변경
# 1개 row 선택
# print('One -> ', c.fetchone())  # 첫 번째 줄을 가리키고 있는 커서 확인 가능

# 지정 row 선택
#print('Three -> ', c.fetchmany(size=3)) # 세 개 가져옴

# 전체 row 선택
#print('All -> ', c.fetchall())  # 이제 한 개밖에 안 남아서 마지막 줄만 가져옴

print()

# 순회 1
rows = c.fetchall() #다 가져오는 거
# for row in rows:
#     print('retrieve1 > ', row)  #조회한 데이터 for문으로 한 줄씩 다 가져옴


# 순회 2
# for row in c.fetchall():
#     print('retrieve2 > ', row)  #위랑 동일

# 순회 3
#for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#    print('retrieve3 > ', row)  # 이것도 위랑 동일한 방법

print()

# WHERE Retrieve1
param1 = (3, )
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())   # id가 3인 c의 내용만 출력됨.
print('param1', c.fetchall())   #원래 다음 데이터 출력하는 건데 param1에 3 하나밖에 없어서 출력되는 데이터 없음

print()

# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d. 위와 동일
print('param1', c.fetchone())   
print('param1', c.fetchall())   

print()

# WHERE Retrieve3
c.execute('SELECT * FROM users WHERE id=:ID', {"ID":5}) # 위와 동일
print('param1', c.fetchone())   
print('param1', c.fetchall())


print()

# WHERE Retrieve4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())   # param에 설정한 두 개 모두 가져옴

print()

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" %(3, 4))    # 위와 동일
print('param5', c.fetchall())

print()

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1":2, "id2":5})   # 위와 동일. id 번호로 원하는 거 찾기.
print('param6', c.fetchall())

print()

# Dump 출력
with conn:  # 데이터들 다 sql문으로 표현하는 파일 만듦
    with open('C:/Users/jinny/OneDrive/바탕 화면/20180368/2021-겨울/FastCampus/BackEnd/Python/1. python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')


# f.close(), conn.close() 모두 호출됨. 바로 위에 있는 conn.iterdump()로 한 번에 자동으로 호출됨을 확인 가능.