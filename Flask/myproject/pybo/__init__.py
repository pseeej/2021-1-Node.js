from flask import Flask

def create_app():   # application factory. flask 내부에서 정의된 함수명
    app = Flask(__name__)   # app 객체 생성

    # create_app 함수에 등록되어있던 hello_pybo 함수 대신 블루프린트 사용하도록 변경
    # 블루프린트 사용하려면 main_views.py 파일에서 생성한 블루프린트 객체 bp 등록하면 됨
    from .views import main_views
    app.register_blueprint(main_views.bp)

    # @app.route('/') # 특정 주소 접속하면 바로 다음 줄에 있는 함수 호출
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    return app  # app 객체 반환