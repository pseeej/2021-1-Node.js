# 질문 등록 폼 클래스 작성

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    # subject, content 속성 포함함.
    # 글자 수에 제한이 있는 제목에는 StringField 이용, 제한 없을 땐 TextAreaField 이용.
    # <input type="text"> 또는 <textarea>와 대응하는 자료형.

    # StringField(폼 라벨, 필드값 검증할 때 사용하는 도구인 validators)
    # validators 종류 : 필수 항목인지 점검하는 DataRequired, 이메일 여부 Email, 길이 점검 Length 등
    # DataRequired 안에 들어간 ~가 오류 메세지로써 출력됨.
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

# 답변 등록할 때 사용할 AnswerForm
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])