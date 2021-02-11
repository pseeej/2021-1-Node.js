from flask import Blueprint, url_for
from werkzeug.utils import redirect

# blueprint class로 생성한 객체인 bp.
# 이름, 모듈명, url prefix값 전달해야함
# url prefix : 특정 파일에 있는 함수의 annotation url 앞에 기본으로 붙일 접두어 url
bp = Blueprint('main', __name__, url_prefix='/')

# 라우트 함수 등록하기
@bp.route('/hello') #localhost:5000/hello
def hello_pybo():   #이거 실행됨
    return 'Hello, Pybo!'

@bp.route('/')  #localhost:5000/으로 가면 
def index():    #이거 실행됨
    # redirect 함수는 입력받은 url로 redirect.
    # url_for은 라우트가 설정된 함수명으로 url을 역으로 찾아줌
    # question(등록된 bp 이름), _list(bp에 등록된 함수명) 순서로 해석되어 함수명 찾아줌
    return redirect(url_for('question._list'))