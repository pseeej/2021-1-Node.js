# 질문 목록, 질문 상세 기능 분리하기

from flask import Blueprint, render_template

from pybo.models import Question

# 블루프린트 객체 생성할 때 question 이름 사용.
# url_prefix = question 사용함으로써 main_views의 url_prefix='/'와는 차이 둠
bp = Blueprint('question',  __name__, url_prefix='/question')

@bp.route('/list/')
# 그냥 list는 python의 예약어라서 사용 불가하므로.
# 질문 목록 받아오기. order_by로 작성일자 기준 역순으로 정렬
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

# question 모델 데이터 중 id값이 question_id인 데이터 조회
# 라우팅 매핑 규칙에 사용한 <int:question_id> 전달됨
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # query.get_or_404는 해당 페이지가 없을 경우 404 페이지 출력해주는 함수
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)