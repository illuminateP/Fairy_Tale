from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..lib.user_service import UserService, authenticate_user

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('비밀번호가 일치하지 않습니다.', 'danger')
            return render_template('register.html')
        user_service = UserService()
        success, message = user_service.register_user(username, email, password)
        if success:
            flash(message, 'success')
            return redirect(url_for('auth_bp.login'))
        else:
            flash(message, 'danger')
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate_user(username, password)
        if user:
            session['user_id'] = user.id
            return redirect(url_for('root_bp.index'))
        else:
            flash('로그인 실패: 아이디 또는 비밀번호가 올바르지 않습니다.')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth_bp.login'))