import os
from flask import Flask
from flask import render_template
from models import db   # models의 db 가져오기

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')    # template이라는 디렉토리 안에서 hello.html을 찾아서 실행하라

if __name__ == '__main__':  # 이 파일이 main일 때

    # 이 내용이 models.py에 있으면 models랑 app이랑 서로 import해서 순환구조 형성됨. 그럼 안되지~ 그래서 app 관련된 설정들 가져옴
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)    # app에 많은 설정값들 초기화
    db.app = app    #db에 app 명시적으로 넣기
    db.create_all() #db 생성
    app.run(host='127.0.0.1',port=5000, debug=True)   # 실행해라
