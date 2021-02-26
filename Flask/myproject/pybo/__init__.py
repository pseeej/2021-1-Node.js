from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# create_app 내에서 생성하면 다른 모듈에서 불러올 수 없기 떄문에 밖에서 생성
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():   # application factory. flask 내부에서 정의된 함수명
    app = Flask(__name__)   # app 객체 생성

    # config.py에 작성한 항목 app.config 환경 변수로 부르기 위해.
    app.config.from_object(config)

    # ORM. 실제 객체 초기화
    db.init_app(app)
    
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    # model들을 플라스크의 migrate 기능이 인식할 수 있도록 함
    from . import models

    # 플라스크 앱 생성 시 블루프린트 적용하기
    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)   # question_views의 bp 객체 등록
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)   # auth_views blueprint 등록
    app.register_blueprint(comment_views.bp) # 블루프린트 추가하기
    app.register_blueprint(vote_views.bp)   # vote_views의 bp 추가

    from .filter import format_datetime
    # 필터 등록
    app.jinja_env.filters['datetime'] = format_datetime

    return app  # app 객체 반환