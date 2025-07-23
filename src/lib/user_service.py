from werkzeug.security import generate_password_hash
from src.utils.model import User
from src.utils.db import db

class UserService:
    def __init__(self):
        pass

    def register_user(self, username, email, password):
        # 이메일 또는 사용자명 중복 확인
        if User.query.filter((User.email == email) | (User.username == username)).first():
            return False, "이미 사용 중인 이메일 또는 사용자명입니다."
        
        # 비밀번호 해시
        hashed_password = generate_password_hash(password)
        
        # 실제 User 모델 객체를 생성하고 DB에 저장
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return True, "회원가입이 성공적으로 완료되었습니다. 로그인해주세요."

    def check_user_credentials(self, email, password):
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return user
        return None

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None 