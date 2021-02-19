# 회원가입 뷰

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        # username으로 데이터 조회해서 이미 등록된 사용자인지 확인
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            # 계정 등록할 때 비밀번호는 입력받은 값 그대로 저장하는 것이 아니라 generate_password_hash 함수로 암호화하여 저장
            user = User(username=form.username.data,
                        password = generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:   # 이미 등록된 사용자일 경우
            flash('이미 존재하는 사용자입니다.')    # 오류 발생
    return render_template('auth/signup.html', form=form)


# POST로 로그인 수행, GET으로 로그인 템플릿 렌더링
@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        # 입력받은 비밀번호랑 hash로 암호화된 기존에 있던 비밀번호의 일치 여부 확인
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            # session : 플라스크 서버를 구동하는 동안에는 영구히 참조할 수 있는 값
            session.clear()
            # session에 user_id값을 저장함으로써 다양한 url 요청에 이 세션 값 사용 가능
            session['user_id'] = user.id     # session에 key('user_id')와 key값(db에서 조회된 사용자의 id값) 저장
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)


# 로그인한 사용자 정보 조회하는 함수 구현
# before_app_request는 모든 route 함수보다 먼저 실행됨
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    # g : flask가 제공하는 context 변수. 요청->응답 과정에서 유효
    # g에 저장 후에는 로그인 검사할 때 session 조사 필요 없음.
    # g.user에 User객체 저장되어 있어 여러가지 사용자 정보(username, email 등)를 추가로 얻어낼 수 있음
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


# 로그아웃
@bp.route('/logout/')
def logout():
    session.clear() # session에 저장된 user_id 삭제됨 => g.user = None
    return redirect(url_for('main.index'))


# 로그인 하고 활동하라고~
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view