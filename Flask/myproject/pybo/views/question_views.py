# 질문 목록, 질문 상세 기능 분리하기

from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db

from ..models import Question
from ..forms import QuestionForm, AnswerForm

# 블루프린트 객체 생성할 때 question 이름 사용.
# url_prefix = question 사용함으로써 main_views의 url_prefix='/'와는 차이 둠
bp = Blueprint('question',  __name__, url_prefix='/question')


@bp.route('/list/')
# 그냥 list는 python의 예약어라서 사용 불가하므로.
# 질문 목록 받아오기. order_by로 작성일자 기준 역순으로 정렬
def _list():
    # localhost:5000/question/list/?page=5에서 5 가져오려고 할 때 사용하는 바로 아래 함수 request.args.get
    page = request.args.get('page', type=int, default=1)    # 페이징 기능 구현
    question_list = Question.query.order_by(Question.create_date.desc())
    # paginate 함수로 페이징 적용. paginate(현재 조회할 페이지의 번호, 페이지마다 보여 줄 게시물의 개수)
    # 해당 함수의 반환값은 Pagination 객체. 페이징 처리를 쉽게 만들어줌
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)


# question 모델 데이터 중 id값이 question_id인 데이터 조회
# 라우팅 매핑 규칙에 사용한 <int:question_id> 전달됨
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    # query.get_or_404는 해당 페이지가 없을 경우 404 페이지 출력해주는 함수
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)


# 질문 등록 라우트 함수 추가하기
# methods=('GET', 'POST')로 질문 전송 방식 수정. default는 get만 가능.
# methods 작성함으로써 질문 등록 라우트에 get이랑 post 방식 포함됨
@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form=QuestionForm() # QuestionForm 클래스의 객체 form 생성

    # request.method == create 함수로 요청된 전송 방식
    # form.validate_on_submit : 전송된 폼 데이터의 정합성 점검 함수. 폼 생성할 때 각 필드에 지정한 점검 항목에 이상 없는지 확인
    # 이상이 없을 경우
    if request.method=='POST' and form.validate_on_submit():
        # 질문 1건 생성
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        # db에 저장
        db.session.add(question)
        db.session.commit()
        # main.index 페이지로 이동하라
        return redirect(url_for('main.index'))

    # request.method=='GET'이면 그대로 질문 등록 화면 보여주기.
    # 템플릿 렌더링할 때 form 객체 전달.
    return render_template('question/question_form.html', form=form)