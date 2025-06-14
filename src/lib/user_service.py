from werkzeug.security import generate_password_hash, check_password_hash
# from models.user_model import User # 실제로는 DB 모델과 연동합니다.

# 임시 사용자 데이터 저장소 (실제로는 DB를 사용해야 합니다)
TEMP_USERS_DB = {}

class UserService:
    def __init__(self):
        # DB 세션 등을 초기화할 수 있습니다.
        pass

    def register_user(self, username, email, password):
        # 이메일 또는 사용자명 중복 확인
        if email in TEMP_USERS_DB or any(user['username'] == username for user in TEMP_USERS_DB.values()):
            return False, "이미 사용 중인 이메일 또는 사용자명입니다."
        
        # 비밀번호 해시
        hashed_password = generate_password_hash(password)
        
        # 새 사용자 정보 저장 (임시)
        # 실제로는 User 모델 객체를 생성하고 DB에 저장합니다.
        # new_user = User(username=username, email=email, password_hash=hashed_password)
        # db.session.add(new_user)
        # db.session.commit()
        TEMP_USERS_DB[email] = {
            'username': username,
            'email': email,
            'password_hash': hashed_password
        }
        
        return True, "회원가입이 성공적으로 완료되었습니다. 로그인해주세요."

    def check_user_credentials(self, email, password):
        user_data = TEMP_USERS_DB.get(email)
        if user_data and check_password_hash(user_data['password_hash'], password):
            # return User.query.filter_by(email=email).first() # 실제로는 DB에서 사용자 객체 반환
            return user_data # 임시로 사용자 정보 반환
        return None 