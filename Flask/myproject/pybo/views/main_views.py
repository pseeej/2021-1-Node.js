from flask import Blueprint

# blueprint class로 생성한 객체인 bp.
# 이름, 모듈명, url prefix값 전달해야함
# url prefix : 특정 파일에 있는 함수의 annotation url 앞에 기본으로 붙일 접두어 url
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello') #localhost:5000/hello
def hello_pybo():   #이거 실행됨
    return 'Hello, Pybo!'

@bp.route('/')  #localhost:5000/으로 가면 
def index():    #이거 실행됨
    return 'Pybo index'