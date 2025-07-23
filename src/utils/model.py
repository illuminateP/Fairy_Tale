from src.utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash

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

def create_test_user():
    if not User.query.filter_by(username='m').first():
        user = User(
            username='m',
            email='m',
            password_hash=generate_password_hash('m')
        )
        db.session.add(user)
        db.session.commit()