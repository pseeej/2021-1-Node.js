# Jump To FLASK
#### from http://wikidocs.net/4542

<hr/>

## 1장 플라스크 개발 준비!
### 1-01 플라스크 시작하기
플라스크는 *마이크로 웹 프레임워크* 라고 불린다. 자유도가 높은 프레임워크.

### 1-02 파이썬 설치하기
<http://www.python.org/downloads>

### 1-03 플라스크 개발 환경 준비하기
#### 가상 환경 만들기
<pre><code>C:\venvs> python -m venv myproject
</code></pre>

#### 가상 환경에 진입하기
<pre><code>C:\venvs> cd C:\venvs\myproject\Scripts
C:\venvs\myproject\Scripts> activate
(myproject) C:\venvs\myproject\Scripts>
</code></pre>
 
#### 가상 환경에서 벗어나기
<pre><code>(myproject) C:\venvs\myproject\Scripts> deactivate
C:\venvs\myproject\Scripts></code></pre>
C:\ 왼쪽에 있던 (myproject)가 사라짐으로써 가상 환경에서 잘 벗어났음을 확인할 수 있음

#### 플라스크 설치하기
<pre><code>(myproject) C:\venvs\myproject\Scripts> pip install Flask</code></pre>

### 1-04 플라스크 프로젝트 생성하기

내가 설명하기 넘 복잡함ㅋ 이거보고 따라하세용 <https://wikidocs.net/81042></br>
저거 따라하고 나면 일반 directory에서 myproject 입력하면 바로 가상 환경을 진입 가능해짐.

### 1-05 파이참 설치하고 사용해보기

~~근데 사실 난 vscode 썼음ㅎㅎ~~

### 1-06 안녕하세요, 파이보!

#### 새 파이썬 파일 작성
###### C:\projects\myproject\pybo.py에 아래 code 작성
<pre>from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_pybo():
    return 'Hello, Pybo!'</pre>
    
#### 플라스크 서버 실행하기
<pre>(myproject) c:\projects\myproject>flask run</pre>

#### 기본 애플리케이션 설정하기 & 플라스크 서버를 개발 환경으로 실행하기
플라스크는 FLASK_APP 환경 변수가 지정되지 않은 경우 자동으로 app.py를 기본 애플리케이션으로 인식함. 
<pre>(myproject) c:\projects\myproject>flask run #으로 환경 변수 지정하기

# 플라스크 서버를 개발 환경으로 실행하기
(myproject) c:\projects\myproject>set FLASK_ENV=development
(myproject) c:\projects\myproject>flask run</pre>

#### 실습을 더 간편하게 환경 변수 추가하기
C:\venvs\myproject.cmd에 아래 코드 입력하면 실행할 때마다 FLASK_APP과 FLASK_ENV 변수를 설정할 필요가 없다. 
<pre>@echo off
cd C:\projects\myproject
set FLASK_APP=pybo
set FLASK_ENV=development
C:\venvs\myproject\scripts\activate</pre>

<hr/>

## 2장 플라스크 개발 기초 공사!
### 2-01 플라스크 기초 다지기

#### pybo 패키지 안에 구성해야 하는 파일과 디렉터리
- DB 처리하는 ```models.py``` 파일: model class들 정의
- 서버로 전송된 폼을 처리하는 ```forms.py``` 파일 : form class 정의
- 화면을 구성하는 ```views 디렉터리```
- CSS, JS, img files 저장하는 ```static 디렉터리```
- HTML 파일 저장하는 ```templates 디렉터리```
- 파이보 프로젝트 설정하는 ```config.py``` 파일 : 환경변수, 데이터베이스 등의 설정 저장

### 2-02 플라스크 애플리케이션 팩토리

- 플라스크 앱 == Flask 클래스로 만든 객체.</br>
- app 객체를 전역으로 사용할 때 발생하는 문제(순환 참조) 예방 위해 애플리케이션 팩토리 사용.</br>
- ```__init__.py``` 파일에 ```create_app()``` 함수 선언.</br>
- _이 때 create_app 함수는 플라스크 내부에서 정의된 함수명._ __애플리케이션 팩토리__
###### 순환 참조 : A 모듈이 B 모듈 참조하고 B 모듈이 다시 A 모듈 참조하는 것 </br>

### 2-03 블루프린트로 라우트 함수 관리하기

blueprint == 청사진. ```URL과 호출되는 함수의 관계 확인할 수 있는 class```

#### 블루프린트 생성하기
<pre>from flask import Blueprint
# Blueprint(이름, 모듈 명, URL prefix)로 생성
bp = Blueprint('main', __name__, url_prefix='/')  # blueprint에서 생성한 객체.

@bp.route('/')
def hello_pybo():
  return 'Hello, Pybo!'</pre>
  
#### 플라스크 앱 생성 시 블루프린트 적용하기
<pre>from .views import main_views
app.register_blueprint(main_views.bp)</pre>

#### 라우트 함수 등록하기
###### C:\projects\myproject\pybo\views\main_views.py 아래 code로 수정
<pre>@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'
    
@bp.route('/')
def index():
    return 'Pybo index'</pre>
    
#### 라우트 함수 동작 확인하기
```localhost:5000```
```localhost:5000/hello```

### 2-04 모델로 데이터 처리하기

### 2-05 질문 목록과 질문 상세 기능 만들기

### 2-06 답변 등록 기능 만들기

### 2-07 화면 예쁘게 꾸미기

### 2-08 부트스트랩으로 더 쉽게 화면 꾸미기

### 2-09 표준 HTML과 템플릿 상속 사용해보기

### 2-10 폼 모듈로 데이터 검증 더 쉽게 하기
