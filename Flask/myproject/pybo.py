from flask import Flask
app = Flask(__name__)   # 플라스크 애플리케이션 생성 코드

@app.route('/') # 특정 주소 접속하면 바로 다음 줄에 있는 함수 호출
def hello_pybo():
    return 'Hello, Pybo!'