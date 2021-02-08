import os
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return render_template('hello.html')    # template이라는 디렉토리 안에서 hello.html을 찾아서 실행하라

if __name__ == '__main__':  # 이 파일이 main일 때
    app.run()   # 실행해라
