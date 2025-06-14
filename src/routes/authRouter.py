from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from ..lib.user_service import UserService

auth_bp = Blueprint('auth_bp', __name__)

class RegistrationForm(FlaskForm):
    username = StringField('사용자명', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('비밀번호 확인', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('가입하기')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        user_service = UserService()
        success, message = user_service.register_user(username, email, password)
        
        if success:
            flash(message, 'success')
            # 로그인 페이지로 리디렉션하거나, 바로 로그인 처리 후 메인 페이지로 이동할 수 있습니다.
            return redirect(url_for('auth_bp.login')) # login 라우트가 있다고 가정
        else:
            flash(message, 'danger')
            
    return render_template('register.html', title='회원가입', form=form)

# 추후 로그인 라우트 등 추가
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # 로그인 폼 처리 로직 (나중에 구현)
    # form = LoginForm()
    # if form.validate_on_submit():
    #     # 로그인 처리
    #     pass
    flash('로그인 기능은 아직 구현되지 않았습니다.', 'info')
    return render_template('login.html', title='로그인') # login.html 템플릿 필요 