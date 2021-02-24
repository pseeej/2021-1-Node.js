# 답변 블루프린트 만들기

from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm
from ..models import Question, Answer
from .auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')

# 답변 등록 라우트 함수
# question_detail.html에서 정의한 form의 method가 post였으므로 여기서도 동일하게 맞춰줘야함
@bp.route('/create/<int:question_id>', methods=('POST',))
# auth_views.py에 속해있는 이 함수 실행함으로써 로그인 여부 확인
@login_required
# question_id는 url에서 전달됨
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():   # 답변 등록에 문제 없으면
        # request.form['content'] == post 폼 방식으로 전송된 데이터 항목 중 name 속성이 content인 값
        content = request.form['content']
        # user = g.user로 작성자 정보 추가
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        # question.answer_set은 질문에 달린 답변들을 의미.
        # question과 answer 모델이 연결되어 있어 backref에 설정한 answer_set 사용 가능
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
        
    # 답변 생성 후 화면 이동하도록 redirect 함수 사용함
    return redirect(url_for('question/question.detail', question=question, form=form))


# 답변 수정
@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer  = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정 권한이 없습니다')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == 'POST':    # 수정 내용 게시
        form = AnswerForm()
        if form.validate_on_submit(): # 수정된 항목이 문제가 없으면
            form.populate_obj(answer)   # form 변수에 있는 데이터를 question 객체에 적용
            answer.modify_date = datetime.now() # 수정 일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id = answer.question.id))
    else:   # 기존 답변 내용 불러오기
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', answer=answer, form=form)

# 답변 삭제
@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user :
        flash('삭제 권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))