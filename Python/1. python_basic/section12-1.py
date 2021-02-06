# section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S') #string format time
print('nowDatetime : ',nowDatetime) #이렇게하면 초가 .단위로는 안 나오네

# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit(바로바로 db에 쓰겠다. Rollback은 삽입되기 이전, 수정되기 이전으로 돌리는 거)
conn = sqlite3.connect('C:/Users/jinny/OneDrive/바탕 화면/20180368/2021-겨울/FastCampus/BackEnd/Python/1. python_basic/resource/database.db', 
isolation_level=None)   #isolation_level = none은 auto commit을 위함.
# 위에 거 하고 나서 설치해둔 db browser for sqlite 들어가서 파일 설정해두면 테이블, 인덱스, 뷰, 트리거 항목 뜰겨.

# Cursor
c = conn.cursor()
print('cursor type : ', type(c))    # class type. sqlite3.cursor

# 테이블 생성 (Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text,\
    phone text, website text, regidate text)") #c.execute(~) ~ 안에 sql문 작성해주면 됨. 이거 실행하고 f5 누르면 새로 테이블이 만들어진 거 확인 가능

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Park', 'park@naver.com', '010-0000-0000',\
    'Park.com', ?)", (nowDatetime,))   #물음표 된 거는 뒤의 ()와 매칭해서 넣음. () 안에 쉼표 꼭 붙여주기
# 이거 한 번 실행되고 나면 이 데이터는 다 삽입이 되는겨. 근데 이후에도 또 이 코드를 그대로 실행하게 되면
# primary key(한 값은 한 번만 나올 수 있음) 속성을 가지고 있는 id에 의해 에러를 발생하게 됨. 그래서 그 다음부터 실행할 땐 이거 주석처리 해야됨

c.execute("INSERT INTO users(id, username, email, phone, website, regidate) VALUES (?,?,?,?,?,?)",
(2, 'Kim', 'Kim@daum.net', '010-1111-1111','Kim.com', nowDatetime))
#한 번에 모든 항목을 채우는 게 아니라 몇 개를 골라서 채우려고 할 때는 이런 방법 이용함. into users(채울 항목의 이름) values(?,?)" (~넣을 내용~)

# Many 삽입 (튜플, 리스트 형태 삽입 가능)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regidate)\
    VALUES(?,?,?,?,?,?)", userList) # 한 번에 여러 개의 데이터 가지고 실행하는 거. userlist에 있는 tuple의 내용을 db에 추가할 수 있게 됨.

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")   # 싹 지워짐
#print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)    # 지운 다음에 지워진 결과값들의 개수 출력함

# 커밋 : isolation_level = None일 경우 자동 반영(auto commit)
# 자동으로 안 되어 있을 때에는 일일이 다 conn.commit() 실행해줘야 함.

# 롤백
# conn.rollback()

# 접속 해제
conn.close()