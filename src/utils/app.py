from flask import Flask
from .db import db  # extensions.py 에서 db 객체 가져오기
from ..routes.authRouter import auth_bp
from ..routes.rootRouter import root_bp
# from models.user_model import User # User 모델 import는 db.create_all() 시점에 SQLAlchemy가 모델을 알 수 있도록 하기 위함이지만,
                                 # 모델 파일 자체에서 db 객체를 사용하므로 명시적 import 없이도 일반적으로 동작합니다.
                                 # 명확성을 위해 또는 특정 케이스에서 필요할 경우 주석 해제 가능합니다.

def create_app():
    app = Flask(__name__, 
                instance_relative_config=True,
                template_folder='../views') # views 폴더를 템플릿 폴더로 지정
    # 기본 설정
    app.config.from_mapping(
        SECRET_KEY='dev',  # 실제 배포 시에는 강력하고 무작위적인 값으로 변경하세요.
        # SQLite 데이터베이스 경로 설정 (instance 폴더 내에 저장)
        SQLALCHEMY_DATABASE_URI='sqlite:///fairytale.db', # instance 폴더 기준 상대 경로
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # instance 폴더가 없다면 생성
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass
    # 위 코드는 파일 기반 설정 (config.py)을 instance 폴더에서 로드할 때 유용하며,
    # SQLite DB 파일은 SQLAlchemy가 경로에 따라 자동으로 생성하므로 필수는 아닙니다.

    # extensions 초기화
    db.init_app(app)

    # 블루프린트 등록
    app.register_blueprint(root_bp)
    app.register_blueprint(auth_bp)
    # 예: app.register_blueprint(auth_bp, url_prefix='/auth') # 인증 관련 URL에 /auth prefix 추가

    # 필요에 따라 다른 블루프린트 (예: 책 질문 관련)도 여기에 등록할 수 있습니다.
    # from routes.book_routes import book_bp # 가상의 책 관련 라우트
    # app.register_blueprint(book_bp)

    # 애플리케이션 컨텍스트 내에서 데이터베이스 테이블 생성
    # 실제 운영 환경에서는 Flask-Migrate와 같은 데이터베이스 마이그레이션 도구를 사용하는 것이 좋습니다.
    return app
