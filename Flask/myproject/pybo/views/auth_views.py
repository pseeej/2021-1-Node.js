# 회원가입 뷰

from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm
from pybo.models import User

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