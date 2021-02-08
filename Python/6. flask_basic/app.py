# venv 설치 : pip3 install virtualenv -> virtualenv flask_fastcampus
# Flask run으로 실행

# flask alchemy 설치 : pip3 install flask-sqlalchemy

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))    # 현재 있는 file의 절대경로 나타남
dbfile = os.path.join(basedir, 'db.sqlite') # db 파일 만들기

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile    # sqlalchemy에 필요한 설정 값 넣어주기. sqlite는 파일만 있으면 됨
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 사용자 요청이 끝날 때마다 commit하도록 함
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 수정 사항에 대한 track을 하겠다

db = SQLAlchemy(app)    # 최상위 class 변수

class Test(db.Model):   # M-V-C에서 data 다루는 model
    __tablename__ = 'test_table'    # db에 들어갈 table명 지정
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique=True)

db.create_all() # 모델 class 만들어져야 db에 등록 가능

@app.route('/')
def hello():
    return 'Hello World!'
