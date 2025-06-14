from extensions import db # 수정: extensions.py에서 db 객체 가져오기
from werkzeug.security import generate_password_hash, check_password_hash

# SQLAlchemy 객체는 app.py 등에서 app과 함께 초기화되어야 합니다.
# 예: db = SQLAlchemy(app)
# 여기서는 임시로 db 객체를 선언만 합니다.
# 실제 사용 시에는 Flask 애플리케이션 컨텍스트 내에서 초기화된 db 객체를 사용해야 합니다.

# db = SQLAlchemy() # 실제로는 app.py에서 db = SQLAlchemy() 로 생성 후 여기서 import 하거나, app.py에서 User 모델을 import합니다.

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False) # 비밀번호 해시 길이 증가

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# 이 모델을 사용하려면 app.py에서 db 객체를 초기화하고,
# app.config에 SQLAlchemy 관련 설정 (예: SQLAlchemy_DATABASE_URI)을 추가해야 합니다.
# 또한 extensions.py의 db 객체를 app과 연결해야 합니다 (db.init_app(app)).
# 예시 app.py 설정:
# from flask import Flask
# from models.user_model import db # User 모델 파일에서 db 객체를 가져옴
# 
# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'your_secret_key'  ㅛ
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db' # 예: SQLite
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 
#     db.init_app(app) # db 객체를 Flask 앱과 연결
# 
#     from routes.auth_routes import auth_bp
#     app.register_blueprint(auth_bp)
# 
#     with app.app_context(): # 애플리케이션 컨텍스트 내에서 DB 테이블 생성
#         db.create_all()
# 
#     return app 