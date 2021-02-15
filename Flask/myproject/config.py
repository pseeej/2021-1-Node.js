import os

# pybo.db 프로젝트의 루트 디렉터리에 저장

BASE_DIR = os.path.dirname(__file__)

# DB 접속 주소.
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQLALCHEMY 이벤트 처리 옵션.
SQLALCHEMY_TRACK_MODIFICATIONS=False

# 웹 사이트 취약점 공격 방지 위해 사용.
SECRET_KEY = "dev"

# flask db init으로 db 관리하는 초기 파일들을 migrations 디렉터리에 자동으로 생성해줌
# 최초 한 번만 수행하면 됨

# 모델 추가하거나 변경할 때는 앞으로
# flask db migrate : 모델 새로 생성하거나 변경할 때 사용
# flask db upgrade : 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용