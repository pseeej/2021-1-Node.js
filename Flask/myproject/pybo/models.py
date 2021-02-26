# 질문 모델 생성하기 위한 파일

# __init__.py에서 생성한 SQLAlchemy 객체 import
from pybo import db

# N:N 관계 정의 위해 db.Table class로 정의하는 table 객체
question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key = True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

# 질문 모델 생성
class Question(db.Model):   # 모든 모델의 기본 클래스인 db.Model 상속받음.
    # 질문 모델 생성. 속성 = db.Column(데이터 타입, ~)
    # primary_key = 기본 키. nullable = 속성에 빈 값을 허용할 것인지.
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    # secondary 설정으로 voter는 N:N 관계이며 question_voter 테이블 참조함을 알려줌
    # 어떤 계정이 a_user라는 객체로 참조되면 backref에 의해 a_user.question_voter_set으로 질문 구할 수 있게 됨
    # backref 설정에 사용하는 이름은 중복 불가
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))

    # question model에 user_id, user field 추가
    # user_id : User model data의 id값을 Question model에 포함시키기 위함
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # user : Question model에서 User model을 참조하기 위한 field
    # backref로 User model data 통해 Question model data 참조
    user = db.relationship('User', backref=db.backref('question_set'))

# answer_voter table 객체
answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

# 답변 모델 생성
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    # 질문 모델과 연결하기 위한 question_id. 어떤 질문에 대한 답변인지 표시하기 위해 foreign key(외부 키) 이용
    # db.ForeignKey(연결할 모델의 속성명, 삭제 연동 설정.)
    # ondelete='CASCADE' : DB에서 쿼리를 이용하여 질문을 삭제하면 해당 질문에 대한 답변도 함께 삭제 
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    # 답변 모델에서 질문 모델을 참조하기 위해 추가.
    # db.relationship(참조할 모델명, 역참조 설정) - 역참조 : 질문에서 답변을 참조하는 것
    question = db.relationship('Question', backref = db.backref('answer_set'))
    
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

    # answer model에 field 추가
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))

# User 모델 생성
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # 자동으로 증가하는 user 모델의 기본 키
    # nullable = False : null값 허용하지 않음
    # unique = True : 같은 값을 저장할 수 없다. 이렇게 해야 중복되어 저장되지 않음
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# 댓글
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))