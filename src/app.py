from flask import Flask
from .utils.db import db  # src/utils/db.py 에서 db 객체 가져오기
from .routes.authRouter import auth_bp # src/routes/authRouter.py 에서 auth_bp 가져오기
from .routes.rootRouter import root_bp   # src/routes/rootRouter.py 에서 root_bp 가져오기

def create_app():
    """Flask 애플리케이션 팩토리 함수"""
    app = Flask(__name__, 
                instance_relative_config=True, 
                template_folder='views')  # 템플릿 폴더를 src/views 로 지정

    # 기본 설정
    app.config.from_mapping(
        SECRET_KEY='dev',  # 실제 배포 시에는 강력하고 무작위적인 값으로 변경하세요.
        # SQLite 데이터베이스 경로 설정 (instance 폴더 내에 fairytale.db로 저장)
        SQLALCHEMY_DATABASE_URI='sqlite:///fairytale.db', 
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # SQLAlchemy 확장 초기화
    db.init_app(app)

    # 블루프린트 등록
    app.register_blueprint(auth_bp) # 인증 관련 블루프린트
    app.register_blueprint(root_bp)   # 루트 경로 및 온보딩 페이지용 블루프린트

    # 애플리케이션 컨텍스트 내에서 데이터베이스 테이블 생성
    # 실제 운영 환경에서는 Flask-Migrate와 같은 데이터베이스 마이그레이션 도구를 사용하는 것이 좋습니다.
    with app.app_context():
        # User 모델을 포함한 모든 db.Model 상속 클래스에 대해 테이블 생성
        # 이 호출 전에 해당 모델 파일이 파이썬에 의해 로드되어 SQLAlchemy가 인식할 수 있어야 합니다.
        import src.models.user_model # 모델을 인식시키기 위해 import (경로 수정)
        #db.create_all()

    return app 